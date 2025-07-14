from aiogram import F, types
from aiogram.dispatcher.router import Router
from aiogram.filters import Command
from aiogram.enums import ContentType
from config import BotConfig
from aichat import Glados

# from . import consts, keyboards, lab_state
config = BotConfig()  # type: ignore
router = Router()
glados = Glados()


@router.message(Command(commands=["start"]))
async def start(msg: types.Message):
    await msg.answer(
        "Поздравляю. Вы запустили систему. Теперь у вас есть 3.5 секунды, чтобы восхититься этим достижением."
    )


@router.message()
async def catch_all_messages(message: types.Message):
    if message.forward_from_chat is None:
        print("Message is not forwarded")
        return
    if message.text and str(message.forward_from_chat.id) == config.channel_id:
        answer = await glados.get_answer(message.text)
        if answer:
            await message.reply(answer)
