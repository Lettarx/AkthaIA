<script>
    async function verificar(e) {
        e.preventDefault()
        const formData = new FormData()

        formData.append('file',img)
        
    }
</script>

<form enctype="multipart/form-data" on:submit={verificar} method="post" >
<input type="text">
<button type="submit" name="imgBase64">Enviar</button>
</form>