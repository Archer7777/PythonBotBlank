from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_reply_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text='Отправить свой контакт ', request_contact=True)
    keyboard_builder.button(text='Отправить геолокацию', request_location=True)
    # keyboard_builder.button(text='Скачать моё резюме')
    # keyboard_builder.button(text='Отправить личное сообщение')
    keyboard_builder.adjust(1, 1)
    return keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=False,
                                      input_field_placeholder='Можете отправить свой контакт, геолокацию и т.д')