# get images with faces from unsplash api and save them to a /images folder

import requests
import os
from dotenv import load_dotenv
from tools import resize, compress

load_dotenv()
UNSPLASH_KEY = os.getenv('UNSPLASH_ACCESS_KEY')
FACE_API_KEY = os.getenv('FACEPP_KEY')
FACE_API_SECRET = os.getenv('FACEPP_SECRET')


def scan_image(id, path):
    face_response = requests.post('https://api-us.faceplusplus.com/facepp/v3/detect', data={
        'api_key': FACE_API_KEY,
        'api_secret': FACE_API_SECRET,
        'image_file': open(path, 'rb'),
        'return_attributes': "gender,age,emotion"
    })
    try:
        face_data = face_response.json()
        face_count = len(face_data['faces']) 
    except Exception as e:
        print(face_data)
        return 0
    print(f"Found {face_count} face(s) in image: {id}\n----------------------\n")
    if face_count == 1:
        src = 'images/face/' + id + '.jpg'
    elif face_count >= 1:
        src = 'images/faces/' + id + '.jpg'
    else:
        src = 'images/no_faces/' + id + '.jpg'

def fix_image(img, path):
    resize(path)
    size = round(os.path.getsize(path) / 1024)
    if size > 2048:
        compress(img['urls']['full'], path)
    
def download_image(image):
    image_response = requests.get(image['urls']['small'])
    image_data = image_response.content
    path = 'images/cache/' + image['id'] + '.jpg'
    with open(path, 'wb') as handler:
        print("Downloading image: " + image['id'])
        handler.write(image_data)
        scan_image(image['id'], path)
        return path

def get_images():
    url = 'https://api.unsplash.com/photos/random?client_id=' + UNSPLASH_KEY + '&count=30&query=people'
    response = requests.get(url)
    data = response.json()
    for image in data:
        p = download_image(image)
        fix_image(image, p)
        scan_image(image['id'], p)