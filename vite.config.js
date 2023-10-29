import {defineConfig} from "vite"
import {resolve} from "path"
import {globSync} from 'glob'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [],
  root: resolve("."),
  base: "/static/",
  server: {
    host: "localhost",
    port: 3000,
    open: false,
    // This ensures assets referenced in CSS files (e.g. fonts)
    // are served with full host during dev
    origin: 'http://localhost:3000',

  },
  resolve: {
    alias: {
      /* Must be equivalent to aliases in tsconfig.json */
      '@': resolve('.'),
    },
    resolve: {
      extensions: [".js", ".vue", ".json"],
    },
  },
  build: {
    outDir: "main/vite-build",
    assetsDir: "",
    manifest: true,
    emptyOutDir: true,
    target: "es2017",
    rollupOptions: {
      input: {
        main: resolve('./main/templates/ts/base.ts'),
      },
      output: {
        chunkFileNames: undefined,
      },
    },
  },
});
