from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import db


async def day_tests_markup(science):
    markup = InlineKeyboardMarkup(row_width=2)
    tests = await db.select_tests(science)
    for test_app in tests:
        markup.insert(InlineKeyboardButton(
            text=f"{test_app[2]}",
            callback_data=test_app[0]
        ))
    markup.row(InlineKeyboardButton(
        text="⬅️ Orqaga",
        callback_data='back'
    ))
    return markup
