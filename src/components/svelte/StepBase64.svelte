<script>
    async function verificar(e) {
        e.preventDefault()
        console.log(e.target[0].value.toString())
        const img = e.target[0].value.toString()
        const imgb = {"imagen_base64": img}
        try {
             const VImgBase64 = await fetch('http://localhost:8001/EvBase68/borrosa/', {
                 method: "POST",
                 headers: {"Content-type": "application/json;charset=UTF-8"},
                 body: JSON.stringify(imgb)
             });
            
             if (!VImgBase64.ok) {
                 console.error('Ocurrió un error durante la solicitud:', Error);
                 setAppStatusError()
                 throw new Error('La solicitud no fue exitosa');
             }
            
             const { docs: resultados } = await VImgBase64.json();
             setAppStatusAnalyze(resultados)
             console.log("resultado",resultados);
         } catch {
             console.error('Ocurrió un error durante la solicitud:', Error);
             setAppStatusError()
        
         }
    }
</script>

<form enctype="text/plain" on:submit={verificar} method="post" >
<input class="mb-3 text-black" type="text"><br>
<button type="submit" name="imagen_base64">Enviar</button>
</form>