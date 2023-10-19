import {expose} from "./utils.ts"

expose({
    sayWelcome,
})

function sayWelcome() {
    console.log('welcome')
}

