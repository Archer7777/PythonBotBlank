from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Связаться со мной', url='tg://user?id=166421650')
    keyboard_builder.button(text='Моё резюме', callback_data='cv')
    keyboard_builder.adjust(1, 1)
    return keyboard_builder.as_markup()
