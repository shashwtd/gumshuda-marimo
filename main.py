import os
from PIL import Image
from dotenv import load_dotenv
from instabot import Bot

load_dotenv()

username = os.getenv('IG_USERNAME')
password = os.getenv('IG_PASSWORD')


def img(img):
    if img.endswith('.png'):
        __ = Image.open(img)
        _img = __.convert('RGB')
        _img.save(f'{img[:-3]}.jpg', 'JPEG')
        os.remove(img)
        return f'{img[:-3]}.jpg'
    return img


def upload(img, caption):
    bot.upload_photo(img, caption=caption)
    # clean_up(img)

    
if __name__ == "__main__":
    bot = Bot()
    bot.login(username=username, password=password)
    upload(img('posts/post.png'), '[test upload]')