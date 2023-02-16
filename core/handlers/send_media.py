from aiogram.types import Message, FSInputFile
from aiogram import Bot
#
#
# async def download_pdf(message: Message, bot: Bot):
#     await message.reply_document(document=open('cv.pdf'))


async def get_cv(message: Message, bot: Bot):
    document = FSInputFile(path='/Users/aleksey/PycharmProjects/PythonBotBlank/cv.pdf')
    await bot.send_document(message.chat.id, document=document, caption='Резюме')