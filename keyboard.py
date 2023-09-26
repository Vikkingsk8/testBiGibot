# Клавиатура для меню и кнопоки для ответов на вопросы

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

menu = [
    [InlineKeyboardButton(text="🧮 Тарифы", url='https://himki.net/internet/'),
     InlineKeyboardButton(text="🤑 Акции", url='https://himki.net/promo/')],
    [InlineKeyboardButton(text="👥 Подключение новых абонентов", url='https://himki.net/checkout/')],
    [InlineKeyboardButton(text="💻 Техническая поддержка", callback_data="support")],
    [InlineKeyboardButton(text="🤔 Другие вопросы", callback_data="other_questions"),
     InlineKeyboardButton(text="📞 Наши контакты", callback_data="contacts")]
]

support_kb = [
    [InlineKeyboardButton(text="Да", callback_data="support_answer_yes"),
     InlineKeyboardButton(text="Нет", callback_data="support_answer_no")]
]


menu = InlineKeyboardMarkup(inline_keyboard=menu)
support_kb = InlineKeyboardMarkup(inline_keyboard=support_kb)

exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])
