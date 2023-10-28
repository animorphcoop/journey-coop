function getLayerData(event: CustomEvent) {
    const eventDetail = event.detail;
    let currentLevelName = eventDetail.current;
    let currentStageName = eventDetail.previous;

    console.log(currentLevelName)
    console.log(currentStageName)

    console.log('event received')

    //TODO: trigger additional processing logic
    return 'OK';
}

function layerEventTrigger(currentLayer: string, previousLayer: string) {
    let appContainer = document.getElementById('app');
    console.log(appContainer)
    if (appContainer) {
        console.log('about to dispatch')
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
