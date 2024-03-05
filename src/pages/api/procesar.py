
from torchvision.transforms.functional import to_tensor
import torch


def evaluarDefectos(img, modelo):
    model = torch.hub.load('./', 'custom', modelo, source='local', force_reload=True)
    results = model(img)
    data = results.pandas().xyxy[0]
    return data

def procesarImg(img, modelo):
    data = evaluarDefectos(img, modelo)
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

    return {"docs": resultados_formateados}