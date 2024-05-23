import requests
# pip install tf-keras
from deepface import DeepFace
import os

url_one = "https://gas-kvas.com/grafic/uploads/posts/2023-09/1695805189_gas-kvas-com-p-kartinki-garri-potter-18.jpg"
url_two = "https://frazy.su/wp-content/uploads/2016/07/regnum_picture_1464862366254511_normal.jpg"


response_one = requests.get(url_one)
response_two = requests.get(url_two)

# current_path = os.path.dirname(os.path.abspath(__file__))
# photos_path = os.path.join(current_path, "photos")

# photo1 = os.path.join(photos_path, 'photo_one.jpg')
# photo2 = os.path.join(photos_path, 'photo_two.jpg')

with open('img1.jpg', 'wb') as file:
    file.write(response_one.content)
    
with open('img2.jpg', 'wb') as file:
    file.write(response_two.content)
    
    
result = DeepFace.verify(img1_path ='img1.jpg', img2_path='img2.jpg', model_name = "VGG-Face")
print(result)
