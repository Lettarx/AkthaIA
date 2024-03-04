import cv2
import numpy as np
import requests
import io
import base64
from PIL import Image as PILImage
# from torchvision.transforms.functional import to_tensor
# import torch
from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel
from typing import List
import uuid

IMAGEDIR = "images/"

app = FastAPI()

@app.post("/prueba/")
async def evaluar_imagen(file: UploadFile = File(...)):
    # try:
    #     contents = await file.read()

       
    #     with open(f"imagen{file.filename}","wb") as f:
    #         f.write(contents)
    #         return {file.filename}
    # except Exception as e:
    #      raise HTTPException(status_code=500, detail=f"Error al procesar la imagen: {str(e)}")
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

# Leemos el modelo
def evaluarDefectos(img, modelo):
    model = torch.hub.load('./', 'custom', modelo, source='local', force_reload=True)
    results = model(img)
    data = results.pandas().xyxy[0]
    return data

class Image(BaseModel):
    url: str


@app.post("/ImgOscura/")
async def evaluar_imagen(image: Image):
    try:
        # Descargar la imagen desde la URL
        response = requests.get(image.url)
        response.raise_for_status()
        print(response.content)  # Imprimir el contenido de la respuesta
        
        img = PILImage.open(io.BytesIO(response.content))
        
        # Convertir la imagen a un formato que se pueda pasar al modelo
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        # Evaluar la imagen con el modelo YOLO
        modelo = 'Modelos/best_160_imgoscuras.pt'  # Nombre del modelo
        resultado = evaluarDefectos(img, modelo)

        # Procesar los resultados
        confidence = resultado['confidence']
        label = resultado['name']

        # Formatear los resultados como un diccionario
        resultados_formateados = []
        for i in range(len(label)):
            resultados_formateados.append({
                "label": label[i],
                "confidence": round(confidence[i] * 100, 1)
            })

        return {"docs": resultados_formateados}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar la imagen: {str(e)}")

@app.post("/Personas/")
async def evaluar_imagen(image: Image):
    try:
        # Descargar la imagen desde la URL
        response = requests.get(image.url)
        response.raise_for_status()
        print(response.content)  # Imprimir el contenido de la respuesta
        
        img = PILImage.open(io.BytesIO(response.content))
        
        # Convertir la imagen a un formato que se pueda pasar al modelo
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        # Evaluar la imagen con el modelo YOLO
        modelo = 'Modelos/epoch_249_640_personas.pt'  # Nombre del modelo
        resultado = evaluarDefectos(img, modelo)

        # Procesar los resultados
        confidence = resultado['confidence']
        label = resultado['name']

        # Formatear los resultados como un diccionario
        resultados_formateados = []
        for i in range(len(label)):
            resultados_formateados.append({
                "label": label[i],
                "confidence": round(confidence[i] * 100, 1)
            })

        return {"docs": resultados_formateados}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar la imagen: {str(e)}")

@app.post("/ImgIluminada/")
async def evaluar_imagen(image: Image):
    try:
        # Descargar la imagen desde la URL
        response = requests.get(image.url)
        response.raise_for_status()
        print(response.content)  # Imprimir el contenido de la respuesta
        
        img = PILImage.open(io.BytesIO(response.content))
        
        # Convertir la imagen a un formato que se pueda pasar al modelo
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        # Evaluar la imagen con el modelo YOLO
        modelo = 'Modelos/best_640_imgiluminadas.pt'  # Nombre del modelo
        resultado = evaluarDefectos(img, modelo)

        # Procesar los resultados
        confidence = resultado['confidence']
        label = resultado['name']

        # Formatear los resultados como un diccionario
        resultados_formateados = []
        for i in range(len(label)):
            resultados_formateados.append({
                "label": label[i],
                "confidence": round(confidence[i] * 100, 1)
            })

        return {"docs": resultados_formateados}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar la imagen: {str(e)}")

@app.post("/ImgMovida/")
async def evaluar_imagen(image: Image):
    try:
        # Descargar la imagen desde la URL
        response = requests.get(image.url)
        response.raise_for_status()
        print(response.content)  # Imprimir el contenido de la respuesta
        
        img = PILImage.open(io.BytesIO(response.content))
        
        # Convertir la imagen a un formato que se pueda pasar al modelo
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        # Evaluar la imagen con el modelo YOLO
        modelo = 'Modelos/best_202_160_imgmovidas.pt'  # Nombre del modelo
        resultado = evaluarDefectos(img, modelo)

        # Procesar los resultados
        confidence = resultado['confidence']
        label = resultado['name']

        # Formatear los resultados como un diccionario
        resultados_formateados = []
        for i in range(len(label)):
            resultados_formateados.append({
                "label": label[i],
                "confidence": round(confidence[i] * 100, 1)
            })

        return {"docs": resultados_formateados}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar la imagen: {str(e)}")

@app.post("/ImgDesenfocada/")
async def evaluar_imagen(image: Image):
    try:
        # Descargar la imagen desde la URL
        response = requests.get(image.url)
        response.raise_for_status()
        print(response.content)  # Imprimir el contenido de la respuesta
        
        img = PILImage.open(io.BytesIO(response.content))
        
        # Convertir la imagen a un formato que se pueda pasar al modelo
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        # Evaluar la imagen con el modelo YOLO
        modelo = 'Modelos/best_320_blur.pt'  # Nombre del modelo
        resultado = evaluarDefectos(img, modelo)

        # Procesar los resultados
        confidence = resultado['confidence']
        label = resultado['name']

        # Formatear los resultados como un diccionario
        resultados_formateados = []
        for i in range(len(label)):
            resultados_formateados.append({
                "label": label[i],
                "confidence": round(confidence[i] * 100, 1)
            })

        return {"docs": resultados_formateados}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar la imagen: {str(e)}")

@app.post("/ParedesEsquinas/")
async def evaluar_imagen(image: Image):
    try:
        # Descargar la imagen desde la URL
        response = requests.get(image.url)
        response.raise_for_status()
        print(response.content)  # Imprimir el contenido de la respuesta
        
        img = PILImage.open(io.BytesIO(response.content))
        
        # Convertir la imagen a un formato que se pueda pasar al modelo
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        # Evaluar la imagen con el modelo YOLO
        modelo = 'Modelos/best_320_paredesesquinas.pt'  # Nombre del modelo
        resultado = evaluarDefectos(img, modelo)

        # Procesar los resultados
        confidence = resultado['confidence']
        label = resultado['name']

        # Formatear los resultados como un diccionario
        resultados_formateados = []
        for i in range(len(label)):
            resultados_formateados.append({
                "label": label[i],
                "confidence": round(confidence[i] * 100, 1)
            })

        return {"docs": resultados_formateados}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar la imagen: {str(e)}")

@app.post('/similitud/')
async def evaluar_silimitud(image:Image, image2:Image):
    # Decodificar la imagen base64 Img1
    imagen_bytes = base64.b64decode(image.url)
    imagen_np = np.frombuffer(imagen_bytes, dtype=np.uint8)
    original = cv2.imdecode(imagen_np, cv2.IMREAD_COLOR)
    
    #IMG2
    imagen_bytes = base64.b64decode(image2.url)
    imagen_np = np.frombuffer(imagen_bytes, dtype=np.uint8)
    image = cv2.imdecode(imagen_np, cv2.IMREAD_COLOR)

    # Check if 2 images are equal shape
    if original.shape == image.shape:
        difference = cv2.subtract(original, image)
        b, g, r = cv2.split(difference)
        #print(cv2.countNonZero(b))
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
            #print("Buenos puntos:", m)

    number_keypoints = 0
    if (len(kp_1) <= len(kp_2)):
        number_keypoints = len(kp_1)
    else:
        number_keypoints = len(kp_2)

    percentage_similarity = len(good_points) / number_keypoints * 100
    mach = "Que tan bueno es el match", percentage_similarity, "%"
    return {"docs": [{"Mach": percentage_similarity}]}

if __name__ == "__main__":
    import uvicorn
    # Ejecuta el servidor usando Uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)