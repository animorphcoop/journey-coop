function getLayerData(event: CustomEvent) {
    const eventDetail = event.detail;
    let currentState = eventDetail.current;
    let nextState = eventDetail.previous;

    let dataToReturn = ''
    console.log(currentState)
    console.log(nextState)

    console.log('event received')

    if (currentState == 'landing') {

        if (nextState == 'login') {
            dataToReturn = initialiseLoginView()

        } else if (nextState == 'nickname') {
            dataToReturn = initialiseNicknameView()
        }
    }

    //TODO: trigger additional processing logic
    return dataToReturn
}


function initialiseLoginView() {
    let feedbackMessage = (document.getElementById('feedback-message'))
    if (feedbackMessage) {
        feedbackMessage.remove();
    }
    return 'OK'
}

function initialiseNicknameView() {
    let topClose = (document.getElementById('top-close'))
    if (topClose) {
        topClose.remove();
    }

    let bottomClose = (document.getElementById('bottom-close'))
    if (bottomClose) {
        bottomClose.remove();
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
