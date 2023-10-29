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

    } else if (currentState == 'login') {
        if (nextState == 'landing') {
            loggedInNav()
            dataToReturn = toggleOverlayEvent()

        }
    } else if (currentState == 'nickname') {
        if (nextState == 'landing') {
            loggedInNav()
            dataToReturn = toggleOverlayEvent()

        }
    } else if (currentState == 'loggedout') {
        if (nextState == 'loggedin') {
            dataToReturn = loggedInNav()

        }
    }

    else if (currentState == 'loggedin') {
        if (nextState == 'loggedout') {
            dataToReturn = loggedOutNav()

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


function loggedInNav() {
    let loginButton = (document.getElementById('login-button'))
    if (loginButton) {
        if (!loginButton.classList.contains('hidden')) {
            loginButton.classList.add('hidden');
        }
    }

    let logoutButton = (document.getElementById('logout-button'))
    if (logoutButton) {
        if (logoutButton.classList.contains('hidden')) {
            logoutButton.classList.remove('hidden');
        }
    }
    return 'OK'
}

function loggedOutNav() {
    let loginButton = (document.getElementById('login-button'))
    if (loginButton) {
        if (loginButton.classList.contains('hidden')) {
            loginButton.classList.remove('hidden');
        }
    }

    let logoutButton = (document.getElementById('logout-button'))
    if (logoutButton) {
        if (!logoutButton.classList.contains('hidden')) {
            logoutButton.classList.add('hidden');
        }
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

function toggleOverlayEvent() {
    let appContainer = document.getElementById('app')
    if (appContainer) {
        appContainer.dispatchEvent(
            new Event('toggleoverlay', {})
        )
    }
    return 'OK'
}


export {getLayerData, layerEventTrigger}
