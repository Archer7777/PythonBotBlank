from aiogram import Bot
from aiogram.types import Message


async def get_start(message: Message, bot: Bot):
    await message.reply(f'Привет {message.from_user.first_name}, я Бот-секретарь Алексея, могу Вам чем нибудь помочь?')
