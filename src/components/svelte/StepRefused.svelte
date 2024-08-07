<script>
    import max from './StepAnalyze.svelte'
    import { resultsEv2, setAppStatus2Accepted, setAppStatus2Refused } from "../../store";
  
    // Obtén los resultados de cada categoría
    const iluminada = $resultsEv2.iluminada;
    const desenfocada = $resultsEv2.desenfocada;
    const movida = $resultsEv2.movida;
    const oscura = $resultsEv2.oscura;
    const pared = $resultsEv2.pared;
    const personas = $resultsEv2.personas; 
</script>

<div class="pb-4">
    {#if desenfocada.length > 0}
        <h3><strong>Imágenes desenfocadas:</strong></h3>
        {#each desenfocada as resultado}
                {#if resultado.confidence === Math.max(...desenfocada.map(p => p.confidence))}
                    {#if resultado.confidence <= 20}
                     <p>No tiene personas</p> 
                        {:else}
                            {#if resultado.label === "Focus"}
                                <p>No esta desenfocada</p> 
                            {:else}
                            <p>Hay una desenfocada en un {resultado.confidence}%</p>
                            {:break}
                            {/if}
                    {/if}
                {/if}
        {/each}
    {:else}
    <p>No hay resultados para imágenes desenfocadas.</p> 
    {/if}
  </div>
  
  <div class="pb-4">
    {#if movida.length > 0}
        <h3><strong>Imágenes movidas:</strong></h3>
        {#each movida as resultado}
                {#if resultado.confidence === Math.max(...movida.map(p => p.confidence))}
                    {#if resultado.confidence <= 20}
                    <p>No tiene personas</p> 
                        {:else}
                            {#if resultado.label === "Not blurry"}
                            <p>No esta movida</p> 
                            {:else}
                            <p>Esta movida en un {resultado.confidence}%</p>
                            {:break}
                            {/if}
                    {/if}
                {/if}
        {/each}
    {:else}
    <p>No hay resultados para imágenes movidas.</p> 
    {/if}
  </div>

  <div class="pb-4">
    {#if oscura.length > 0}
        <h3><strong>Imágenes oscuras:</strong></h3>
        {#each oscura as resultado}
                {#if resultado.confidence === Math.max(...oscura.map(p => p.confidence))}
                    
                        {#if ( resultado.label === "FullDark")||(resultado.label ==="LightDark")} 
                            <p>Esta oscura en un {resultado.confidence}%</p>
                            {:break}
                            
                        {:else}
                        <p>No esta oscura</p> 
                        {/if}
                {/if}
        {/each}
    {:else}
     <p>No hay resultados para imágenes oscuras.</p> 
    {/if}
  </div>

  <div class="pb-4">
    {#if iluminada.length > 0}
        <h3><strong>Imágenes iluminadas:</strong></h3>
        {#each iluminada as resultado}
                {#if resultado.confidence === Math.max(...iluminada.map(p => p.confidence))}
                    {#if ( resultado.label != "normal")&& (resultado.confidence >= 60)} 
                    <p>Esta iluminada en un {resultado.confidence}%</p>
                    {:break}
                    
                    {:else}
                     <p>No esta iluminada</p> 
                    {/if}
                    
                {/if}
        {/each}
    {:else}
        <p>No hay resultados para imágenes con personas.</p>
    {/if}
  </div>

  <div class="pb-4">
    {#if pared.length > 0}
        <h3><strong>Imágenes con paredes:</strong></h3>
        {#each pared as resultado}
                {#if resultado.confidence === Math.max(...pared.map(p => p.confidence))}
                    {#if resultado.confidence <= 60}
                            <p>No tiene paredes</p>
                        {:else}
                            {#if resultado.label === ""}  
                                <p>No tiene pared o esquina</p>
                            {:else}
                                <p>Hay una pared en un {resultado.confidence}%</p> 
                                {:break}
                            {/if}
                    {/if}
                {/if}
        {/each}
    {:else}
        <p>No hay resultados para imágenes con paredes.</p> 
    {/if}
  </div>

  <div class="pb-4">
    {#if personas.length > 0}
        <h3><strong>Imágenes con personas:</strong></h3>
        {#each personas as resultado}
                {#if resultado.confidence === Math.max(...personas.map(p => p.confidence))}
                    {#if resultado.confidence <= 60}
                        <p>No tiene personas</p>
                    {:else}
                        {#if resultado.label === ""} 
                        <p>No tiene personas</p> 
                        {:else}
                        <p>Hay una persona en un {resultado.confidence}%</p>
                        {:break}
                        
                        {/if}
                    {/if}
                {/if}
        {/each}
    {:else}
     <p>No hay resultados para imágenes con personas.</p> 
    {/if}
  </div>
