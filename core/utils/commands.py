from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Начало работы'
        ),

        BotCommand(
            command='help',
            description='Помощь'
        ),

        BotCommand(
            command='cancel',
            description='Сбросить'
        ),

        BotCommand(
            command='contact',
            description='Связаться со мной'
        ),

        BotCommand(
            command='cv',
            description='Моё резюме'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
