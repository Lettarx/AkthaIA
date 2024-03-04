<script>
    import { Alert, P } from 'flowbite-svelte';
    import { APP_STATUS2, appStatus2 } from '../../store'
    import StepLoading from './StepLoading.svelte';
    import StepUpload from './StepUpload.svelte';
    import StepAccepted from './StepAccepted.svelte';
    import StepRefused from './StepRefused.svelte';
</script>

<!-- EL $ en la store es para observar el valor que tienen -->

{#if $appStatus2 == APP_STATUS2.INIT}
    <StepUpload/>
{:else if $appStatus2 == APP_STATUS2.LOADING}
    <StepLoading/>
{:else if $appStatus2 == APP_STATUS2.ACCEPTED}
    <StepAccepted/>
{:else if $appStatus2 == APP_STATUS2.REFUSED}
    <StepRefused/>
{:else if $appStatus2 == APP_STATUS2.ERROR}
    <Alert>
        <span class="font-medium">Algo malo a pasado!</span>
        Hay un error en la aplicación
    </Alert>
{:else}
    <Alert>
        <span class="font-medium">Acción no reconocida</span>
        Este estado de la aplicación no está conocido
    </Alert>
{/if}
