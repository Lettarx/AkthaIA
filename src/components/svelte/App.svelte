<script>
    import { Alert, P } from 'flowbite-svelte';
    import { APP_STATUS, appStatus, StatusImg1, StatusImg2 } from '../../store'
    import StepLoading from './StepLoading.svelte';
    import StepUpload from './StepUpload.svelte';
    import StepAccepted from './StepAccepted.svelte';
    import StepRefused from './StepRefused.svelte';
    import StepAnalyze from './StepAnalyze.svelte';
    import StepBase64 from './StepBase64.svelte';
</script>

<!-- EL $ en la store es para observar el valor que tienen -->

{#if $appStatus == APP_STATUS.INIT}
    <StepUpload/>
{:else if $appStatus == APP_STATUS.LOADING}
    <StepLoading/>
{:else if $appStatus == APP_STATUS.ACCEPTED}
    <StepAccepted/>
{:else if $appStatus == APP_STATUS.REFUSED}
    <StepRefused/>
{:else if $appStatus == APP_STATUS.ANALYZE}
    <StepAnalyze/>
{:else if $appStatus == APP_STATUS.BASE64}
    <StepBase64/>
{:else if $StatusImg1 == true && $StatusImg2 == true}
<Alert class="mb-10">
    <span class="font-medium">Empezar a evaluar similitud</span>
    
</Alert>
{:else if $appStatus == APP_STATUS.ERROR}
    <Alert class="mb-10">
        <span class="font-medium">Algo malo a pasado!</span>
        Hay un error en la aplicación
    </Alert>
{:else}
    <Alert class="mb-10">
        <span class="font-medium">Acción no reconocida</span>
        Este estado de la aplicación no está conocido
    </Alert>
{/if}



