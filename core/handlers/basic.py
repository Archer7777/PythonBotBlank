from aiogram import Bot
from aiogram.types import Message
from core.keyboards.reply import get_reply_keyboard


async def get_start(message: Message):
    await message.reply(f'Привет {message.from_user.first_name}, я Бот-секретарь Алексея, могу Вам чем нибудь помочь?',
                        reply_markup=get_reply_keyboard())


async def get_location(message: Message, bot: Bot):
    await message.answer(f'Вы отправили свою геолокацию!\r\a'
                         f'{message.location.latitude}\r\n{message.location.longitude}')


async def get_photo(message: Message, bot: Bot):
    await message.answer(f'Отлично. Вы отправили картинку, я сохраню ее себе')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo.jpg')


async def get_hello(message: Message, bot: Bot):
    await message.answer(f'И Вам здравствуйте!')


