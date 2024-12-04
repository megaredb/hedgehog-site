import { defineConfig } from "astro/config";
import { loadEnv } from "vite";
import tailwind from "@astrojs/tailwind";
import react from "@astrojs/react";

// https://astro.build/config
export default defineConfig({
  integrations: [
    tailwind({
      configFile: "./tailwind.config.mjs",
      applyBaseStyles: false,
    }),
    react(),
  ],
});
