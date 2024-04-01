<script>
import { img1, img2 } from "../../store";
let resultados = { docs: [] }; 
async function EvSimilitud() {
    const formData = new FormData()
    formData.append('file1',$img1)
    formData.append('file2', $img2)
    try {
        const resImgDarks = await fetch('http://localhost:8001/similitud/', {
            method: "POST",
            body: formData
        });
        
        // if (!resImgDarks.ok) {
        //     console.error('Ocurrió un error durante la solicitud:', Error);
        //     throw new Error('La solicitud no fue exitosa');
        // }
        
        resultados = await resImgDarks.json();
    } catch {
        console.error('Ocurrió un error durante la solicitud:', Error);
    }
}
EvSimilitud()
</script>

{#if resultados.docs.length > 0}
    {#each resultados.docs as resultado}
        <div> La similitud es del {Math.trunc(resultado.Mach)}%</div>
    {/each}
{/if}