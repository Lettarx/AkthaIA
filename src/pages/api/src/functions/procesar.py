
from torchvision.transforms.functional import to_tensor
import torch
from fastapi import UploadFile, File, HTTPException
from PIL import Image as PILImage
import io
import cv2
import numpy as np


modelos = {
    "iluminada"  : 'src/modelos/best640iluminadas.pt',
    "oscura"     : 'src/modelos/best160oscuras.pt',
    "movida"     : 'src/modelos/epoch2950640movimiento.pt',
    "desenfocada": 'src/modelos/best640blur.pt',
    "pared"      : 'src/modelos/best640blur.pt',
    "personas"   : 'src/modelos/best2360160personas.pt'
}

def evaluarDefectos(img, modelo):
    model = torch.hub.load('./', 'custom', modelo, source='local', force_reload=True)
    results = model(img)
    data = results.pandas().xyxy[0]
    return data

def unirModelos():
    pass

def formatearData(data):
    # Procesar los resultados
    confidence = data['confidence']
    label = data['name']

    # Formatear los resultados como un diccionario
    resultados_formateados = []
    for i in range(len(label)):
        resultados_formateados.append({
            "label": label[i],
            "confidence": round(confidence[i] * 100, 1)
        })

    return resultados_formateados



def procesarImg(img):
    #Preparar imagen
    image = PILImage.open(io.BytesIO(img))
    image_np = np.array(image)
    imgLista = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    #Evaluar con el modelo correspondiente
    dataIluminada   = evaluarDefectos(imgLista, modelos.get('iluminada'))
    dataOscura      = evaluarDefectos(imgLista, modelos.get('oscura'))
    dataMovida      = evaluarDefectos(imgLista, modelos.get('movida'))
    dataDesenfocada = evaluarDefectos(imgLista, modelos.get('desenfocada'))
    dataPared       = evaluarDefectos(imgLista, modelos.get('pared'))
    dataPersonas    = evaluarDefectos(imgLista, modelos.get('personas'))

    # Crear la estructura de salida
    output = {
        "docs": {
            "iluminada"  : formatearData(dataIluminada),
            "oscura"     : formatearData(dataOscura),
            "movida"     : formatearData(dataMovida),
            "desenfocada": formatearData(dataDesenfocada),
            "pared"      : formatearData(dataPared),
            "personas"   : formatearData(dataPersonas)
        }
    }

    return output
    


def evaluarSimilitud(i1,i2):
    #preparar imagen
    image = PILImage.open(io.BytesIO(i1))
    image_np = np.array(image)
    img1 = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    image = PILImage.open(io.BytesIO(i2))
    image_np = np.array(image)
    img2 = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)


    # Check if 2 images are equal shape
    if img1.shape == img2.shape:
        difference = cv2.subtract(img1, img2)
        b, g, r = cv2.split(difference)
        if (cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0):
            print('Las imagenes son completamente iguales')
            return {"docs": [{"Mach": 100}]}

    # Sift and Flann
    shift = cv2.xfeatures2d.SIFT_create()
    kp_1, desc_1 = shift.detectAndCompute(img1, None)
    kp_2, desc_2 = shift.detectAndCompute(img2, None)

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