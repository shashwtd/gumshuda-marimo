from PIL import Image
import tinify
import os
from dotenv import load_dotenv

load_dotenv()
TINIFY_KEY = os.getenv('TINIFY_KEY')


def resize(path):
    image = Image.open(path)
    width, height = image.size
    if width > 4096 or height > 4096:
        if width > height:
            new_width = 4096
            new_height = int(height * (new_width / width))
        else:
            new_height = 4096
            new_width = int(width * (new_height / height))
        image = image.resize((new_width, new_height))
        image.save(path)
        print(f"Resized image to {new_width}x{new_height}")

def compress(url, path):
    source = tinify.from_url("https://tinypng.com/images/panda-happy.png")
    source.to_file(path)
    return print("Compressed image: " + url)