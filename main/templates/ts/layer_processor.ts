function getLayerData(event: CustomEvent) {
    const eventDetail = event.detail;
    let currentLevelName = eventDetail.current;
    let currentStageName = eventDetail.previous;

    console.log(currentLevelName)
    console.log(currentStageName)

    console.log('event received')

    const dataToReturn = initialiseLogin()
    //TODO: trigger additional processing logic
    return dataToReturn
}


function initialiseLogin() {
    let feedbackMessage = (document.getElementById('feedback-message'))
    if (feedbackMessage) {
        feedbackMessage.remove();
    }
    return 'OK'
}

function layerEventTrigger(currentLayer: string, previousLayer: string) {
    let appContainer = document.getElementById('app')
    if (appContainer) {
        appContainer.dispatchEvent(
            new CustomEvent('layerchange', {
                detail: {
                    current: currentLayer,
                    previous: previousLayer,
                },
            })
        )
    }
}

export {getLayerData, layerEventTrigger}
