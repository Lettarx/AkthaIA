from fastapi import FastAPI, UploadFile, File
from src.functions.procesar import procesarImg, evaluarSimilitud
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuración de CORS
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:4321"
    # Agrega aquí otros orígenes permitidos si es necesario
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.post("/CriteriosEvaluacion/")
async def evaluar_imagen(file: UploadFile = File(...)):

    img = await file.read()
    
    return procesarImg(img)


@app.post('/similitud/')
async def evaluar_imagen(img1: UploadFile = File(...), img2: UploadFile = File(...)):
    return evaluarSimilitud(img1,img2)
    

if __name__ == "__main__":
    import uvicorn
    # Ejecuta el servidor usando Uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)