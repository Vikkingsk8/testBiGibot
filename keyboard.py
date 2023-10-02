# Клавиатура для меню и кнопоки для ответов на вопросы

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

menu = [
    [InlineKeyboardButton(text="🧮 Тарифы", callback_data='tariffs'),
     InlineKeyboardButton(text="🤑 Акции", url='https://himki.net/promo/'),
     InlineKeyboardButton(text="💳 Оплата", callback_data='payment')],
    [InlineKeyboardButton(text="👥 Подключение новых абонентов", url='https://himki.net/checkout/')],
    [InlineKeyboardButton(text="💻 Техническая поддержка", callback_data="support")],
    [InlineKeyboardButton(text="🤔 Другие вопросы", callback_data="other_questions"),
     InlineKeyboardButton(text="📞 Наши контакты", callback_data='contacts')]
]

tariffs_kb = [
    [InlineKeyboardButton(text="Химки", url="https://himki.net/internet/"),
     InlineKeyboardButton(text="Солнечногорск", url="https://soln.ru/internet/")]
]

payment_kb = [
    [InlineKeyboardButton(text="Химки", url="https://himki.net/subscribers/oplata-uslug/oplata-bankovskimi-kartami/"),
     InlineKeyboardButton(text="Солнечногорск",
                          url="https://soln.ru/subscribers/oplata-uslug/oplata-bankovskimi-kartami/")]
]

# support_kb = [
#     [InlineKeyboardButton(text="Да", callback_data="support_answer_yes"),
#      InlineKeyboardButton(text="Нет", callback_data="support_answer_no")]
#]

menu = InlineKeyboardMarkup(inline_keyboard=menu)
# support_kb = InlineKeyboardMarkup(inline_keyboard=support_kb)
payment_kb = InlineKeyboardMarkup(inline_keyboard=payment_kb)
tariffs_kb = InlineKeyboardMarkup(inline_keyboard=tariffs_kb)

exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Выйти в меню", callback_data="menu")]])
