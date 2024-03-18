<script>
    import { Alert, P } from 'flowbite-svelte';
    import { APP_STATUS2, appStatus2 } from '../../store'
    import StepLoading2 from './app2/StepLoading2.svelte';
    import StepUpload2 from './app2/StepUpload2.svelte';
    import StepAccepted2 from './app2/StepAccepted2.svelte';
    import StepRefused2 from './app2/StepRefused2.svelte';
    import StepAnalyze2 from './app2/StepAnalyze2.svelte';
    import StepBase642 from './app2/StepBase642.svelte';
</script>

<!-- EL $ en la store es para observar el valor que tienen -->

{#if $appStatus2 == APP_STATUS2.INIT}
    <StepUpload2/>
{:else if $appStatus2 == APP_STATUS2.LOADING}
    <StepLoading2/>
{:else if $appStatus2 == APP_STATUS2.ACCEPTED}
    <StepAccepted2/>
{:else if $appStatus2 == APP_STATUS2.REFUSED}
    <StepRefused2/>
{:else if $appStatus2 == APP_STATUS2.ANALYZE}
    <StepAnalyze2/>
{:else if $appStatus2 == APP_STATUS2.BASE64}
    <StepBase642/>
{:else if $appStatus2 == APP_STATUS2.ERROR}
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
