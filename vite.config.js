import { defineConfig } from "vite"
import { resolve } from "path"
import { globSync } from 'glob'

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
            input: Object.fromEntries(
                /* We define ALL the ts files as entries

                   For prod build those entries get written to:
                     journey/static/build/manifest.json

                   .. and vite_asset reads from there.

                 */
                globSync('main/templates/**/*.ts').map(filename =>
                    [filename.replace(/\.ts$/, ''), filename]
                )
            ),
            output: {
                chunkFileNames: undefined,
            },
        },
    },
});
