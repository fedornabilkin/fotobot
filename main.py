import telebot
from telebot import types
import shutil
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

TB_TOKEN = os.getenv('TB_TOKEN')
TB_RECIPIENT = os.getenv('TB_RECIPIENT')
IMG_FOLDER = os.getenv('IMG_FOLDER')
IMG_OLD_FOLDER = os.getenv('IMG_OLD_FOLDER')

bot = telebot.TeleBot(TB_TOKEN)

def my_scan():
    photos = get_photos()
    if photos != []:
        for photo in photos:
            if os.path.isdir(IMG_FOLDER + photo):
                continue
            file = open(IMG_FOLDER + photo, 'rb')
            bot.send_photo(TB_RECIPIENT, file)
            file.close()
            copy(IMG_FOLDER + photo, IMG_OLD_FOLDER + photo)


def get_photos():
    return os.listdir(IMG_FOLDER)


def copy(source, dest):
    shutil.copyfile(source, dest)
    os.remove(source)

if __name__ == '__main__':
    my_scan()
