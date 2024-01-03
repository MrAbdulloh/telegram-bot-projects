from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

btnSub = KeyboardButton("❤️ ПОДПИСКА")
btnSettings = KeyboardButton("⚙️ НАСТРОЙКИ")
mainMeny = ReplyKeyboardMarkup(resize_keyboard=True)
mainMeny.add(btnSub)
mainMeny.add(btnSettings)

sub_inline_markup = InlineKeyboardMarkup(row_width=1)

btnSubMonth = InlineKeyboardButton(text='Месяц - 150 рублей', callback_data='submonth')

sub_inline_markup.insert(btnSubMonth)
