import { writable } from 'svelte/store'

//Para APP1
export const APP_STATUS={
    INIT:0,
    LOADING:1,
    ANALYZE:2,
    ACCEPTED:3,
    REFUSED:4,
    BASE64:5,
    ACCEPTEDIMG1:false,
    ACCEPTEDIMG2:false,
    ERROR:-1
}

const ejemploresults = {

    iluminada: [],
  
    oscura: [],
  
    movida: [ { label: 'Not blurry', confidence: 90.2 } ],
  
    desenfocada: [ { label: 'Focus', confidence: 86.2 } ],
  
    pared: [ { label: 'Focus', confidence: 86.2 } ],
  
    personas:[
  
      { label: 'Person', confidence: 51.6 },
  
      { label: 'Person', confidence: 46.8 },
  
      { label: 'Person', confidence: 45.9 },
  
      { label: 'Person', confidence: 39.8 },
  
      { label: 'Person', confidence: 39.1 },
  
      { label: 'Person', confidence: 37.8 },
  
      { label: 'Person', confidence: 36.5 },
  
      { label: 'Person', confidence: 31.8 },
  
      { label: 'Person', confidence: 28.6 },
  
      { label: 'Person', confidence: 27.8 }
  
    ]
  
  }

export const resultsEv = writable(ejemploresults)

export const appStatus = writable(APP_STATUS.INIT)
export const StatusImg1 = writable(false)
export const StatusImg2 = writable(false)
export const img1 = writable()
export const img2 = writable()

export const setAppStatusLoading = () => {
    appStatus.set(APP_STATUS.LOADING)
}
export const setAppStatusInit = () => {
    appStatus.set(APP_STATUS.INIT)
}
export const setAppStatusAnalyze = (results) => {
    appStatus.set(APP_STATUS.ANALYZE)
    resultsEv.set(results)
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
export const setAppStatusImg1 = () => {
    StatusImg1.set(true)
}
export const setAppStatusImg2 = () => {
    StatusImg2.set(true)
}
export const setAppStatusBase64 = () => {
    appStatus.set(APP_STATUS.BASE64)
}
export const setImg1 = (imagen1:File) => {
    img1.set(imagen1)
}
export const setImg2 = (imagen2:File) => {
    img2.set(imagen2)
}
//Para APP2
export const APP_STATUS2={
    INIT:0,
    LOADING:1,
    ANALYZE:2,
    ACCEPTED:3,
    REFUSED:4,
    BASE64:5,
    ERROR:-1
}

export const resultsEv2 = writable(ejemploresults)

export const appStatus2 = writable(APP_STATUS2.INIT)

export const setAppStatus2Loading = () => {
    appStatus2.set(APP_STATUS2.LOADING)
}
export const setAppStatus2Init = () => {
    appStatus2.set(APP_STATUS2.INIT)
}
export const setAppStatus2Accepted = () => {
    appStatus2.set(APP_STATUS2.ACCEPTED)
}
export const setAppStatus2Refused = () => {
    appStatus2.set(APP_STATUS2.REFUSED)
}
export const setAppStatus2Error = () => {
    appStatus2.set(APP_STATUS2.ERROR)
}
export const setAppStatus2Analyze = (results) => {
    appStatus2.set(APP_STATUS2.ANALYZE)
    resultsEv2.set(results)
}
export const setAppStatus2Base64 = () => {
    appStatus2.set(APP_STATUS2.BASE64)
}