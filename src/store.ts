import { writable } from 'svelte/store'

export const APP_STATUS={
    INIT:0,
    LOADING:1,
    ACCEPTED:2,
    REFUSED:3,
    ERROR:-1
}

export const appStatus = writable(APP_STATUS.INIT)

export const setAppStatusLoading = () => {
    appStatus.set(APP_STATUS.LOADING)
}
export const setAppStatusInit = () => {
    appStatus.set(APP_STATUS.INIT)
}
export const setAppStatusAccepted = () => {
    appStatus.set(APP_STATUS.ACCEPTED)
}
export const setAppStatusRefused = () => {
    appStatus.set(APP_STATUS.REFUSED)
}
export const setAppStatusError = () => {
    appStatus.set(APP_STATUS.ERROR)
}

export const APP_STATUS2={
    INIT:0,
    LOADING:1,
    ACCEPTED:2,
    REFUSED:3,
    ERROR:-1
}

export const appStatus2 = writable(APP_STATUS.INIT)

export const setAppStatus2Loading = () => {
    appStatus.set(APP_STATUS2.LOADING)
}
export const setAppStatus2Init = () => {
    appStatus.set(APP_STATUS2.INIT)
}
export const setAppStatus2Accepted = () => {
    appStatus.set(APP_STATUS2.ACCEPTED)
}
export const setAppStatus2Refused = () => {
    appStatus.set(APP_STATUS2.REFUSED)
}
export const setAppStatus2Error = () => {
    appStatus.set(APP_STATUS2.ERROR)
}


