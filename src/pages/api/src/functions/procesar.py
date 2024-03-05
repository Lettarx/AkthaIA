
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

def evaluarSimilitud(img1,img2):
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