import cognitive_face as CF

# About
# this script uses Microsoft Azure's Face API. First must install on terminal
# pip install cognitive_face
# requires valid subscription to Azure, as well as a created Face API service

# to try out, go to
# https://azure.microsoft.com/en-us/services/cognitive-services/face/

KEY = 'c1c45b21473a4c6dbd02a2155d1cddd8'  # subscription key
CF.Key.set(KEY)

BASE_URL = 'https://eastus2.api.cognitive.microsoft.com/face/v1.0/'  # service URL specific to my location
CF.BaseUrl.set(BASE_URL)

# URL points to image in my git repository
img_url = 'https://raw.githubusercontent.com/filipmazurek/emotion_reader/master/captured_image.jpg'
faces = CF.face.detect(img_url, False, False, "emotion")  # may change parameters to return other data
print(faces)
