<script>
    import max from './StepAnalyze.svelte'
</script>

<!-- 

  <div class="pb-4">
    {#if desenfocada.length > 0}
        <h3><strong>Imágenes desenfocadas:</strong></h3>
        {#each desenfocada as resultado}
                {#if resultado.confidence === Math.max(...desenfocada.map(p => p.confidence))}
                    {#if resultado.label === "Focus"}
                        <p>No esta desenfocada</p>
                    {:else}
                    <table class="table-auto">
                        <tr>
                        <th>Label</th>
                        <th>Confidence</th>
                        </tr>
                        <tr>
                            <td>{resultado.label}</td>
                            <td>{resultado.confidence}%</td>
                        </tr>
                    </table> 
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
                    {#if resultado.label === "Not blurry"}
                        <p>No esta movida</p>
                    {:else}
                    <table class="table-auto">
                        <tr>
                        <th>Label</th>
                        <th>Confidence</th>
                        </tr>
                        <tr>
                            <td>{resultado.label}</td>
                            <td>{resultado.confidence}%</td>
                        </tr>
                    </table> 
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
                    {#if resultado.label === "Lit"}  revisar la etiqueta LightDark 
                        <p>No esta oscura</p>
                    {:else}
                    <table class="table-auto">
                        <tr>
                        <th>Label</th>
                        <th>Confidence</th>
                        </tr>
                        <tr>
                            <td>{resultado.label}</td>
                            <td>{resultado.confidence}%</td>
                        </tr>
                    </table> 
                    {/if}
                {/if}
        {/each}
    {:else}
        <p>No hay resultados para imágenes oscuras.</p>
    {/if}
  </div>

  <div class="pb-4">
    {#if pared.length > 0}
        <h3><strong>Imágenes con paredes:</strong></h3>
        {#each pared as resultado}
                {#if resultado.confidence === Math.max(...pared.map(p => p.confidence))}
                    {#if resultado.label === ""}  revisar lo de la esquina, pared o rincon 
                        <p>No tiene pared o esquina</p>
                    {:else}
                    <p>Hay una pared en un {resultado.confidence}%</p>
                     <table class="table-auto">
                        <tr>
                        <th>Label</th>
                        <th>Confidence</th>
                        </tr>
                        <tr>
                            <td>{resultado.label}</td>
                            <td>{resultado.confidence}%</td>
                        </tr>
                    </table>  
                    {/if}
                {/if}
        {/each}
    {:else}
        <p>No hay resultados para imágenes con paredes.</p>
    {/if}
  </div> -->

<div class="pb-4">
    <h3><strong>Imágenes con personas:</strong></h3>
    <p>hay personas en un  {max.personas}%</p>
                
</div> 

