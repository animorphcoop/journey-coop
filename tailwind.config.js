/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */
import plugin from "tailwindcss/plugin.js"

import forms from "@tailwindcss/forms"
import typography from "@tailwindcss/typography"
import aspectRatio from "@tailwindcss/aspect-ratio"

export default {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        'main/templates/base.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        './main/templates/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        './main/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
        extend: {
            colors: {
                main: {
                    DEFAULT: '#111827'
                },//add tailwind colors here
                greyish: {
                    DEFAULT: '#e9efe2'
                },
                grey: {
                    DEFAULT: '#F1F1F1'
                },
                limey: {
                    DEFAULT: '#dcf6a4'
                },
                minty: {
                    DEFAULT: '#b7f8bb'
                },
                violety: {
                    DEFAULT: '#bea4f5'
                }
            }

        },
        fontFamily: {
            'sans': ['Inter'],
        }
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
