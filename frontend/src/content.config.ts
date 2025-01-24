import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

export const volumes = defineCollection({
  loader: glob({
    pattern: "*.json",
    base: "./src/content/volumes",
  }),
  schema: z.object({
    id: z.number(),
    title: z.string(),
    pictures: z.array(z.string()),
    chapters: z.array(z.object({ title: z.string(), uri: z.string() })),
  }),
});

export const collections = {
  volumes,
};
