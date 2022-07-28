import telebot
from telebot import types
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

TB_TOKEN = os.getenv('TB_TOKEN')
IMG_FOLDER = os.getenv('IMG_FOLDER')

bot = telebot.TeleBot(TB_TOKEN)


def my_scan():
    photos = get_photos()
    if photos != []:
        for photo in photos:
            file = open(IMG_FOLDER + photo, 'rb')
            bot.send_photo(364484915, file)
            file.close()
            os.remove(IMG_FOLDER + photo)


def get_photos():
    return os.listdir(IMG_FOLDER)


if __name__ == '__main__':
    my_scan()
    # get_text_messages('a')
