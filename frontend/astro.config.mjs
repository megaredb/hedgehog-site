import { defineConfig } from "astro/config";
import { loadEnv } from "vite";
import tailwind from "@astrojs/tailwind";
import vue from "@astrojs/vue";

// https://astro.build/config
export default defineConfig({
  integrations: [
    tailwind({
      configFile: "./tailwind.config.mjs",
      applyBaseStyles: false,
    }),
    vue(),
  ],
});
