<script>
    import { Alert } from 'flowbite-svelte';
    import { APP_STATUS, appStatus, StatusImg1, StatusImg2 } from '../../store'
    import AnalyzeSimilitud from './AnalyzeSimilitud.svelte';
</script>

<!-- EL $ en la store es para observar el valor que tienen -->

{#if $StatusImg1 == true && $StatusImg2 == true}
    <AnalyzeSimilitud/>
{:else if $appStatus == APP_STATUS.ERROR}
    <Alert class="mb-10">
        <span class="font-medium">Algo malo a pasado!</span>
        Hay un error en la aplicación
    </Alert>
{:else}
    <div></div>
{/if}

