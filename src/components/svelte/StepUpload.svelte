<script lang="ts">
    import { setAppStatusAccepted, setAppStatusError, setAppStatusLoading, setAppStatusRefused } from '../../store'
    import Dropzone from "svelte-file-dropzone";
  
    let files = {
      accepted: [],
      rejected: []
    };
  
    async function handleFilesSelect(e) {
      const { acceptedFiles, fileRejections } = e.detail;
      files.accepted = [...files.accepted, ...acceptedFiles];
      files.rejected = [...files.rejected, ...fileRejections];

      if (acceptedFiles.length > 0){
        const formData = new FormData()
        const img = acceptedFiles[0] as File
        formData.append('file',img)

        setAppStatusLoading()
        try {
            const resImgDarks = await fetch('http://localhost:8000/pruebamodel/', {
                method: "POST",
                body: formData
            });
            
            if (!resImgDarks.ok) {
                console.error('Ocurrió un error durante la solicitud:', Error);
                setAppStatusError()
                throw new Error('La solicitud no fue exitosa');
            }
            
            const { docs: resultados } = await resImgDarks.json();
            setAppStatusAccepted(resultados)
            console.log("resultado",resultados);
        } catch {
            console.error('Ocurrió un error durante la solicitud:', Error);
            setAppStatusError()
        }
        
      }
    }
  </script>
  {#if files.accepted.length == 0}
    <Dropzone 
        multiple={false}
        noClick={false}
        on:drop={handleFilesSelect}>Arrastra y suelta aqui tu imagen
    </Dropzone>
  {/if}

  <ol>
    {#each files.accepted as item}
      <li>{item.name}</li>
    {/each}
  </ol>