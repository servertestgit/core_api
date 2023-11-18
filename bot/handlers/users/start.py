import requests
from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from loader import dp, bot
from save import save_user
from data.config import ADDRES

users = dict()


@dp.message_handler(Command('start'))
async def show_menu1(message: Message):
    await message.reply("<b>Xush kelibsiz! \n\nKirish uchun loginni bosing</b> \n👉🏻 /login")


@dp.message_handler(Command('login'))
async def show_menu1(message: Message):
    users[message.from_user.id] = dict()
    usr = save_user(message)
    if usr.status_code == 201:
        usr_txt = usr.text
        user_id = message.from_user.id
        user_profile_photos = await bot.get_user_profile_photos(user_id)
        if user_profile_photos.total_count > 0:
            await bot.send_message(chat_id=user_id, text="Loading...")
            photo = user_profile_photos.photos[0][-1]
            file_id = photo.file_id
            file = await bot.get_file(file_id)
            file_path = file.file_path
            await bot.download_file(file_path, f'avatar_{user_id}.jpg')
            image_path = f'avatar_{user_id}.jpg'
            with open(image_path, 'rb') as image_file:
                data = {'username': message.from_user.id}
                files = {'avatar': image_file}
                requests.post(
                    f'{ADDRES}api/register/avatar-update/', data=data, files=files)
        await message.reply(f"<b>Kirish kodi:</b> {usr_txt}")

    elif usr.status_code == 200:
        usr_txt = usr.text
        await message.reply(f"<b>Yangi kirish kodi:</b> {usr_txt}")
