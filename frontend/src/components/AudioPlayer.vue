<!-- <script setup lang="ts">
import { useStore } from "@nanostores/vue";

import { playing, volume, volumeId } from "@/ts/audio-player";


const $playing = useStore(playing);
const $volume = useStore(volume);
const $volumeId = useStore(volumeId);
</script> -->

<script setup lang="ts">
import { computed, ref, watch } from "vue";
import { useStore } from "@nanostores/vue";

import {
  $currentTome,
  $currentChapter,
  $savedData,
} from "@/components/AudioPlayer";

import volumeXIcon from "@/images/volume-x.svg";
import volumeIcon from "@/images/volume-0.svg";
import volume1Icon from "@/images/volume-1.svg";
import volume2Icon from "@/images/volume-2.svg";
import playIcon from "@/images/play.svg";
import pauseIcon from "@/images/pause.svg";

function updateSavedData() {
  let savedVolumeData = $savedData.value[currentTome.value!.id];

  if (!savedVolumeData) {
    savedVolumeData = {
      latestChapter: currentChapter.value,
      chaptersData: {},
    };
  }

  savedVolumeData.latestChapter = currentChapter.value;
  savedVolumeData.chaptersData[currentChapter.value] = {
    time: audio.currentTime,
  };

  let newValue = $savedData.get();
  newValue[currentTome.value!.id] = savedVolumeData;

  $savedData.set(newValue);

  localStorage.setItem("savedData", JSON.stringify($savedData.get()));
}

function secondsToTime(seconds: number) {
  let date = new Date(0);

  date.setSeconds(seconds || 0);

  return date.toISOString().substring(11, 19);
}

function updateAudio(autoPlay: boolean = false) {
  audio.src = currentTome.value!.chapters[currentChapter.value].uri;
  audio.autoplay = autoPlay;
  audio.volume = volume.value / 100;

  currentTime.value = audio.currentTime =
    $savedData.value[currentTome.value!.id]?.chaptersData[currentChapter.value]
      ?.time || 0;

  audio.load();
}

const volumeIcons = [volumeIcon, volume1Icon, volume2Icon];

const playing = ref(false);
const volume = ref(parseInt(localStorage.getItem("volume")!) || 100);
const audio = new Audio();
const duration = ref(0);
const currentTime = ref(0);

const currentVolumeIcon = computed(() =>
  volume.value
    ? volumeIcons[Math.ceil(volume.value / (100 / volumeIcons.length)) - 1]
    : volumeXIcon,
);

const currentTome = useStore($currentTome);
const currentChapter = useStore($currentChapter);

watch(volume, () => {
  audio.volume = volume.value / 100;
  localStorage.setItem("volume", volume.value.toString());
});

watch(currentChapter, () => {
  currentTime.value = audio.currentTime =
    $savedData.value[currentTome.value!.id]?.chaptersData[currentChapter.value]
      ?.time || 0;
  playing.value = false;

  updateSavedData();
  updateAudio(true);
});

watch(playing, () => {
  if (playing.value) {
    audio.play();
    return;
  }
  audio.pause();
});

audio.addEventListener("canplay", () => {
  if (audio.autoplay) {
    playing.value = true;
  }

  audio.autoplay = false;
  duration.value = audio.duration;
});

audio.addEventListener("timeupdate", () => {
  currentTime.value = audio.currentTime;

  if (audio.ended) {
    playing.value = false;
  }
});

const onSystemCalledPlayingChange = () => {
  playing.value = !audio.paused;
};

audio.addEventListener("play", () => {
  onSystemCalledPlayingChange();
});

audio.addEventListener("pause", () => {
  onSystemCalledPlayingChange();
});

setInterval(() => {
  if (!playing.value) {
    return;
  }

  updateSavedData();
}, 5000);

updateAudio();
</script>

<template>
  <div
    id="audio-player"
    class="max-h-full min-w-80 flex-grow rounded-sm bg-hedgehog-0 p-3 shadow-md shadow-hedgehog-5"
  >
    <p id="audio-player-title" class="mb-2 text-center text-lg font-bold">
      {{ currentTome?.chapters[currentChapter].title }} -
      {{ secondsToTime(audio.duration) }}
    </p>

    <div class="flex items-center justify-center gap-2 text-center">
      <button
        id="play"
        class="interactive flex min-h-8 min-w-8 items-center justify-center rounded-full bg-hedgehog-0"
        v-on:click="
          {
            playing = !playing;
          }
        "
      >
        <img
          id="play-icon"
          format="svg"
          alt="Play"
          class="h-6 w-6"
          loading="eager"
          :src="playing ? pauseIcon.src : playIcon.src"
        />
      </button>

      <span
        id="time"
        class="w-[5.3rem] shrink-0 rounded-2xl bg-hedgehog-0 p-1 px-2 text-center"
      >
        {{ secondsToTime(currentTime) }}
      </span>

      <div class="flex h-8 w-full items-center rounded-full bg-hedgehog-0 p-2">
        <input
          id="track"
          type="range"
          class="h-full grow"
          min="0"
          :max="duration"
          :value="currentTime"
          @input="
            currentTime = parseInt(($event.target! as HTMLInputElement).value);
            audio.currentTime = currentTime;
            updateSavedData();
          "
        />
      </div>

      <button id="volume" class="h-8 w-8 items-center">
        <div
          class="interactive flex h-8 w-8 items-center justify-center rounded-full bg-hedgehog-0"
        >
          <img
            id="volume-icon"
            :src="currentVolumeIcon.src"
            format="svg"
            alt="Volume"
            class="h-6 w-6"
            loading="eager"
          />
        </div>

        <div
          id="volume-slider-container"
          class="relative bottom-[12.5rem] items-center rounded-2xl bg-hedgehog-0 py-2 text-sm shadow-md shadow-hedgehog-5 backdrop-blur-sm"
        >
          <input
            id="volume-slider"
            type="range"
            class="vertical h-32 grow"
            min="0"
            max="100"
            v-bind:value="volume"
            @input="
              volume = parseInt(($event.target! as HTMLInputElement).value)
            "
          />

          <p id="volume-slider-value">{{ volume }}</p>
        </div>
      </button>
    </div>
  </div>
</template>

<style lang="scss">
#volume {
  #volume-slider-container {
    transition: all ease 0.2s;

    scale: 0;
    transform: translateY(100%);
  }

  &:hover {
    #volume-slider-container {
      scale: 1;
      transform: none;
    }
  }
}

.interactive {
  transition: scale ease 0.2s;

  &:hover {
    scale: 1.1;
  }
}

input[type="range"] {
  -webkit-appearance: none;
  @apply cursor-pointer appearance-none overflow-hidden rounded-2xl bg-hedgehog-0 outline-none;

  &::-webkit-slider-thumb {
    @apply h-4 w-2 appearance-none rounded-full bg-hedgehog-4;

    box-shadow: -404px 0 0 400px silver;
  }

  &.vertical {
    writing-mode: vertical-lr;
    direction: rtl;

    &::-webkit-slider-thumb {
      @apply h-2 w-4;
      box-shadow: 0 400px 0 393px white;
    }
  }
}
</style>
