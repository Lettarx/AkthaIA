<script lang="ts">
    import { resultsEv, setAppStatusAccepted, setAppStatusRefused, setAppStatusImg1 } from "../../store";
  
    // Obtén los resultados de cada categoría
    const iluminada = $resultsEv.iluminada;
    const desenfocada = $resultsEv.desenfocada;
    const movida = $resultsEv.movida;
    const oscura = $resultsEv.oscura;
    const pared = $resultsEv.pared;
    const personas = $resultsEv.personas;

    export let accepted = {
            iluminada : false,
            desenfocada : false,
            movida: false,
            oscura: false,
            pared: false,
            personas: false
        }
    
    const analizar = ()=>{
        if (desenfocada.length > 0) {
            desenfocada.map(resultado => {
                if (resultado.confidence === Math.max(...desenfocada.map(p => p.confidence))) {
                    if (resultado.confidence <= 20) {
                        accepted.desenfocada = false;
                    } else {
                        if (resultado.label === "Focus") {
                            accepted.desenfocada = true;
                        }
                    }
                }
            });
        
        } else {
            accepted.desenfocada = true;
        }

        if (movida.length > 0) {
            movida.map(resultado => {
                if (resultado.confidence === Math.max(...movida.map(p => p.confidence))) {
                    if (resultado.confidence <= 60) {
                        accepted.movida = true;
                    } else {
                        if (resultado.label === "Not blurry") {
                            accepted.movida = true;
                        }
                    }
                }
            });
        } else {
            accepted.movida = true;
        }
        if (oscura.length > 0){
            oscura.map(resultado => {
                if (resultado.confidence === Math.max(...oscura.map(p => p.confidence))){
                    if( (resultado.label === "FullDark") &&(resultado.confidence >=60)){
                        accepted.oscura = false
                    } else accepted.oscura = true 
                    
                }
            });
        }else{
            accepted.oscura = true
        }
        if (iluminada.length > 0){
            iluminada.map(resultado => {
                if (resultado.confidence === Math.max(...iluminada.map(p => p.confidence))){
                   if( ( resultado.label != "normal")&& (resultado.confidence >= 80)){
                    
                   }else accepted.iluminada = true
                    
                }
            });
        }else accepted.iluminada = true
        
        if (pared.length > 0){
            pared.map(resultado => {
                if (resultado.confidence === Math.max(...pared.map(p => p.confidence))){
                    if (resultado.confidence >= 60 && resultado.label != ""){
                     accepted.pared = true
                    }
                }
            });
        } else accepted.pared = true
 
    if (personas.length > 0){
        personas.map(resultado => {
                if (resultado.confidence === Math.max(...personas.map(p => p.confidence))){
                    if (resultado.confidence <= 80){
                        accepted.personas = true} 
                }else{
                        if( resultado.label === ""){ 
                            accepted.personas = true
                        }else{
                        }
                }
            });
        } else accepted.personas = true
        
        if (accepted.iluminada === true && accepted.desenfocada === true && accepted.movida === true && accepted.oscura === true && accepted.personas === true){
            setAppStatusImg1()
            setAppStatusAccepted()
        } else setAppStatusRefused()

    }  
    analizar()

</script>
