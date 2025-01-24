import { atom } from "nanostores";
import type { VolumeData } from "@/lib/utils";

export type SavedData = Record<
  number,
  { latestChapter: number; chaptersData: Record<number, { time: number }> }
>;

export const $savedData = atom<SavedData>(
  JSON.parse(localStorage.getItem("savedData") || "{}") as SavedData,
);
export const $currentTome = atom<VolumeData | null>(null);
export const $currentChapter = atom(0);
