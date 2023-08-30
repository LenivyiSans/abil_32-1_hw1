from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp


async def echo_ban(message: types.Message):
    ban_words = ["блять","сука", "ебаный", "бля"]

    if message.chat.id == 1751557503:
        for word in ban_words:
            if word in message.text.lower().replace(" ", ""):
                await bot.delete_message(
                    chat_id=message.chat.id,
                    message_id=message.message_id
                )
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=f"Сам ты такой, {message.from_user.username}!"
                )


def register_chat_actions_handlers(dp: Dispatcher):
    dp.register_message_handler(echo_ban)
