from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import bot
from aiogram import types, Dispatcher
from database.sql_commands import Database
from const import START_MENU_TEXT

async def start_button(message: types.Message):
    print(message)
    Database().sql_insert_users(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name
    )
    with open("C:/Users/TM-PC/PycharmProjects/My_first_bot/media/bots-instagram-logo-round-blue.png", "rb") as photo:
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption=START_MENU_TEXT
        )

async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "Следущий Вопрос",
        callback_data="button_call_1"
    )
    button_call_2 = InlineKeyboardButton(
        "Ничего не делает",
        callback_data="button_call_2"
    )
    markup.row(
        button_call_1,
        button_call_2
    )

    question = "Кто у нас придумал питон"
    options = [
        "Shrek",
        "Hahatun",
        "Linus Torvalds",
        "Guido Van Rossumn"
    ]

    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=options,
        is_anonymous=False,
        type="quiz",
        correct_option_id=3,
        reply_markup=markup
    )


async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "Male",
        callback_data="answer_male"
    )
    button_call_2 = InlineKeyboardButton(
        "Female",
        callback_data="answer_female"
    )
    markup.row(
        button_call_1,
        button_call_2
    )
    await bot.send_message(
        chat_id=call.message.chat.id,
        text='Male or Female',
        reply_markup=markup
  )


async def answer_male(call: types.CallbackQuery):
    await call.bot.send_message(
        chat_id=call.message.chat.id,
        text='You are Male'
    )


async def answer_female(call: types.CallbackQuery):
    await call.bot.send_message(
        chat_id=call.message.chat.id,
        text='You are Female'
    )


def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(start_button, commands=["start"])
    dp.register_message_handler(quiz_1, commands=["quiz"])
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(answer_male, lambda call: call.data == "answer_male")
    dp.register_callback_query_handler(answer_female, lambda call: call.data == "answer_female")
