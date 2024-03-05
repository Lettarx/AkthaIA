import cv2
import numpy as np
import io
import base64
from PIL import Image as PILImage
from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel
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

@app.post("/prueba/")
async def evaluar_imagen(file: UploadFile = File(...)):
    img = await file.read()
    image = PILImage.open(io.BytesIO(img))
    image_np = np.array(image)
    original = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    
    #IMG2
    img = cv2.imread('img1.jpg')
    image = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Check if 2 images are equal shape
    if original.shape == image.shape:
        difference = cv2.subtract(original, image)
        b, g, r = cv2.split(difference)
        if (cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0):
            print('Las imagenes son completamente iguales')
            return {"docs": [{"Mach": 100}]}

    # Sift and Flann
    shift = cv2.xfeatures2d.SIFT_create()
    kp_1, desc_1 = shift.detectAndCompute(original, None)
    kp_2, desc_2 = shift.detectAndCompute(image, None)

    index_params = dict(algorithm=0, trees=5)
    search_params = dict()

    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(desc_1, desc_2, k=2)

    # 2) Check for similarities between the 2 images
    good_points = []
    for m, n in matches:
        if m.distance < 0.6*n.distance:
            good_points.append(m)

    number_keypoints = 0
    if (len(kp_1) <= len(kp_2)):
        number_keypoints = len(kp_1)
    else:
        number_keypoints = len(kp_2)

    percentage_similarity = len(good_points) / number_keypoints * 100
    mach = "Que tan bueno es el match", percentage_similarity, "%"
    return {"docs": [{"Mach": percentage_similarity}]}

@app.post("/pruebamodel/")
async def evaluar_imagen(file: UploadFile = File(...)):
    img = await file.read()
    image = PILImage.open(io.BytesIO(img))
    
    image_np = np.array(image)
    original = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    return procesarImg(original,'src/modelos/best640.pt')


class Image(BaseModel):
    url: str


@app.post("/ImgOscura/")
async def evaluar_imagen(file: UploadFile = File(...)):
    try:
        img = await file.read()
        image = PILImage.open(io.BytesIO(img))
        model = 'best640.pt'
        image_np = np.array(image)
        original = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
        return procesarImg(original,model)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar la imagen: {str(e)}")

@app.post("/Personas/")
async def evaluar_imagen(file: UploadFile = File(...)):
    try:
        img = await file.read()
        image = PILImage.open(io.BytesIO(img))
        model = 'Modelos/epoch_249_640_personas.pt'
        image_np = np.array(image)
        original = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
        return procesarImg(original,model)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar la imagen: {str(e)}")

@app.post("/ImgIluminada/")
async def evaluar_imagen(file: UploadFile = File(...)):
    try:
        img = await file.read()
        image = PILImage.open(io.BytesIO(img))
        model = 'Modelos/best_640_imgiluminadas.pt'
        image_np = np.array(image)
        original = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
        return procesarImg(original,model)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar la imagen: {str(e)}")


@app.post("/ImgMovida/")
async def evaluar_imagen(file: UploadFile = File(...)):
    try:
        img = await file.read()
        image = PILImage.open(io.BytesIO(img))
        model = 'Modelos/best_202_160_imgmovidas.pt'
        image_np = np.array(image)
        original = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
        return procesarImg(original,model)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar la imagen: {str(e)}")

@app.post("/ImgDesenfocada/")
async def evaluar_imagen(file: UploadFile = File(...)):
    try:
        img = await file.read()
        image = PILImage.open(io.BytesIO(img))
        model = 'Modelos/best_320_blur.pt'
        image_np = np.array(image)
        original = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
        return procesarImg(original,model)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar la imagen: {str(e)}")
       

@app.post("/ParedesEsquinas/")
async def evaluar_imagen(file: UploadFile = File(...)):
    try:
        img = await file.read()
        image = PILImage.open(io.BytesIO(img))
        model = 'Modelos/best_320_paredesesquinas.pt'
        image_np = np.array(image)
        original = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
        return procesarImg(original,model)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar la imagen: {str(e)}")


@app.post('/similitud/')
async def evaluar_silimitud(image:Image, image2:Image):
    #IMG1
    imagen_bytes = base64.b64decode(image.url)
    imagen_np = np.frombuffer(imagen_bytes, dtype=np.uint8)
    original = cv2.imdecode(imagen_np, cv2.IMREAD_COLOR)
    
    #IMG2
    imagen_bytes = base64.b64decode(image2.url)
    imagen_np = np.frombuffer(imagen_bytes, dtype=np.uint8)
    image = cv2.imdecode(imagen_np, cv2.IMREAD_COLOR)

    return evaluarSimilitud(original,image)
    

if __name__ == "__main__":
    import uvicorn
    # Ejecuta el servidor usando Uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)