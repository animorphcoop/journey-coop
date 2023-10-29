// https://vitejs.dev/config/build-options.html#build-modulepreload
import 'vite/modulepreload-polyfill'

import htmx from 'htmx.org'
import Alpine from 'alpinejs'

import '@/static/css/main.css'
import '@/static/css/tailwind.css'
import {getLayerData, layerEventTrigger} from "./layer_processor.ts"

import {expose} from "./utils.ts"

expose({htmx, Alpine, getLayerData, layerEventTrigger})



/**
 * Delay starting Alpine until after all our scripts are downloaded
 * This ensures we can use any of our exposed functions in x-init attributes.
 *
 * "The DOMContentLoaded event fires when the HTML document has been completely parsed,
 * and all deferred scripts (<script defer src="…"> and <script type="module">) have
 * downloaded and executed."
 * https://developer.mozilla.org/en-US/docs/Web/API/Window/DOMContentLoaded_event
 */
window.addEventListener('DOMContentLoaded', () => {
    Alpine.start()
})
