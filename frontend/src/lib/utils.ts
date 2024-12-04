import { type ClassValue, clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export function getVolumePreview(volumeId: number): string {
  return `/images/volumes/preview/${volumeId}.png`;
}

export function getVolumeImage(volumeId: number): string {
  return `/images/volumes/${volumeId}.png`;
}
