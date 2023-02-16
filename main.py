import contextlib

from aiogram import Dispatcher, Bot
from aiogram import F
from aiogram.filters import Command, CommandStart

from core.handlers.basic import get_start, get_photo, get_hello, get_inline, get_location
from core.handlers.send_media import get_cv
from core.settings import settings
from core.utils.commands import set_commands
from core.filters.iscontact import IsTrueContact
from core.handlers.contact import get_true_contact, get_fake_contact
import asyncio
import logging


async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот запущен!')


async def stop_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен!')


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_hello, F.text.lower().in_({'Привет', 'привет'}))
    dp.message.register(get_inline, Command(commands='contact'))
    dp.message.register(get_cv, Command(commands='cv'))
    dp.message.register(get_location, F.content_type == 'location')
    dp.message.register(get_true_contact, F.content_type == 'contact', IsTrueContact())
    dp.message.register(get_fake_contact, F.content_type == 'contact')
    dp.message.register(get_start, Command(commands=['start', 'run']))

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":

    with contextlib.suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(start())
