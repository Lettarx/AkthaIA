<script>
    import { setAppStatusAnalyze , setAppStatusError, setAppStatusLoading, setAppStatusRefused } from '../../store'
    
    async function verificar(e) {
        e.preventDefault()
        try {
            // Obtener el valor del input
            const imgBase64 = event.target.elements.imgb64.value;

            // Construir el objeto a enviar en el cuerpo de la solicitud
            const bodyData = {
                imagen_base64: imgBase64
            };
            setAppStatusLoading()

            const VImgBase64 = await fetch('http://localhost:8001/CriteriosEvaluacionBase64/', {
                method: "POST",
                headers: {
                'Content-Type': 'application/json' 
                },
                body: JSON.stringify(bodyData) 
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
    <input name="imgb64"class="mb-3 text-black" type="text"><br>
    <button type="submit" name="imagen_base64">Enviar</button>
</form>