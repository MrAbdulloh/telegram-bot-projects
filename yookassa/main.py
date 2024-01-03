import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType
import markups as nav

TOKEN = '6461270257:AAFD0EhHu5CfIsFUDOgQAIzSzdzswJzaJJo'  # @mybookinglessonbot_bot
YOOTOKEN = '381764678:TEST:74711'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, text='Добрый день', reply_markup=nav.mainMeny)


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        if message.text == "❤️ ПОДПИСКА":
            await bot.send_message(message.from_user.id, text="Описание возможностей подписки",
                                   reply_markup=nav.sub_inline_markup)


@dp.callback_query_handler(text='submonth')
async def sub_month(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_invoice(chat_id=call.from_user.id, title='Оформление подписки',
                           description='test description product', payload='month_sub', provider_token=YOOTOKEN,
                           currency="RUB", start_parameter='test_bot', prices=[{'label': "Руб", 'amount': 15000}])


@dp.pre_checkout_query_handler()
async def process_pro_check_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_pay(message: types.Message):
    if message.successful_payment.invoice_payload == 'month_sub':
        await bot.send_message(message.from_user.id, text='Вам выдана подпсико на месяц')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
