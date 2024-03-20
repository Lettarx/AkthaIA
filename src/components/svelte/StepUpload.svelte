<script lang="ts">
    import { setAppStatusAccepted, setAppStatusAnalyze , setAppStatusBase64, setAppStatusError, setAppStatusLoading, setAppStatusRefused } from '../../store'
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
            const resImgDarks = await fetch('http://10.58.49.37:8001/CriteriosEvaluacion/', {
                method: "POST",
                body: formData
            });
            
            if (!resImgDarks.ok) {
                console.error('Ocurrió un error durante la solicitud:', Error);
                setAppStatusError()
                throw new Error('La solicitud no fue exitosa');
            }
            
            const { docs: resultados } = await resImgDarks.json();
            setAppStatusAnalyze(resultados)
            console.log("resultado",resultados);
        } catch {
            console.error('Ocurrió un error durante la solicitud:', Error);
            setAppStatusError()
        }
        
      }
    }
  </script>
  {#if files.accepted.length == 0}
    <button 
      class="inline-block px-4 py-2 mb-3 text-slate-200 bg-slate-600 border border-gray-800 rounded hover:bg-blue-600 hover:text-white transition duration-300"
      on:click={setAppStatusBase64}>
      Usar imagen con Base64</button>
    <div class="mb-10 aspect-auto">
      <Dropzone 
          disableDefaultStyles
          containerClasses="flex flex-col items-center p-7 border-2 border-dashed border-gray-800 bg-slate-600 text-gray-400 outline-none transition duration-300 focus:border-blue-600"
          multiple={false}
          noClick={false}
          on:drop={handleFilesSelect}>Selecciona tu imagen o Arrastra y sueltala
      </Dropzone>
    </div>
  {/if}

  <ol>
    {#each files.accepted as item}
      <li>{item.name}</li>
    {/each}
  </ol>