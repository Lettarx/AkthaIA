<script lang="ts">
    import { resultsEv, setAppStatusAccepted, setAppStatusAnalyze, setAppStatusRefused } from "../../store";
  
    // Obtén los resultados de cada categoría
    const iluminada = $resultsEv.iluminada;
    const desenfocada = $resultsEv.desenfocada;
    const movida = $resultsEv.movida;
    const oscura = $resultsEv.oscura;
    const pared = $resultsEv.pared;
    const personas = $resultsEv.personas;

    const accepted = {
            iluminada : false,
            desenfocada : false,
            movida: false,
            oscura: false,
            pared: false,
            personas: false
        }
    
    export const max = {
            iluminada : 0,
            desenfocada : 0,
            movida: 0,
            oscura: 0,
            pared: 0,
            personas: 0
    }

    personas.map((result)=>{
            if (result.confidence === Math.max(...personas.map(p => p.confidence))){
                if (result.label === "Normal") {accepted.personas = true}
                
                else { max.personas = result.confidence
                    // setAppStatusRefused()
                } 
            }
        })
    
    console.log(max.personas)
    const analizar = ()=>{
        

        if ((iluminada.length = 0)&&(desenfocada.length = 0)&&(movida.length = 0)&&(oscura.length = 0)&&(pared.length = 0)&&(personas.length = 0)){
            setAppStatusAccepted()
        } 

    }  
</script>

<h1>Imagen 1:</h1>
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
                    {#if ( resultado.label != "normal")} 
                    <p>Esta iluminada en un {resultado.confidence}%</p>
                    
                    {:else}
                        <p>No esta iluminada</p>
                    {/if}
                    <!-- {#if resultado.confidence <= 60}
                            <p>imagenes iluminadas</p>
                        {:else}
                            {#if resultado.label === ""}  
                                <p>No esta iluminada</p>
                            {:else}
                            <p>Esta iluminada en un {resultado.confidence}%</p>
                            
                            {/if}
                    {/if} -->
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
                            <p>No tiene personas</p>
                        {:else}
                            {#if resultado.label === ""}  revisar lo de la esquina, pared o rincon 
                                <p>No tiene pared o esquina</p>
                            {:else}
                            <p>Hay una pared en un {resultado.confidence}%</p>
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
                        {#if resultado.label === ""}  revisar lo de la esquina, pared o rincon 
                            <p>No tiene personas</p>
                        {:else}
                        <p>Hay una persona en un {resultado.confidence}%</p>
                        
                        {/if}
                    {/if}
                {/if}
        {/each}
    {:else}
        <p>No hay resultados para imágenes con personas.</p>
    {/if}
  </div>

  