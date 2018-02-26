import cognitive_face as CF

KEY = 'c1c45b21473a4c6dbd02a2155d1cddd8'  # subscription key
CF.Key.set(KEY)

BASE_URL = 'https://eastus2.api.cognitive.microsoft.com/face/v1.0/'
CF.BaseUrl.set(BASE_URL)

# currently using example jpg URL
img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
faces = CF.face.detect(img_url, False, False, "emotion")
print(faces)
