from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message
import asyncio

import keyboard as kb
import text

import utils

from time import sleep

router = Router()


# Стартовый  хэндлер
@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)


@router.message(Command("contacts"))
async def contacts_handler(msg: Message):
    await msg.answer(text.contact, reply_markup=kb.menu)


@router.callback_query(Command("support"))
async def support_handler_answer(callback: types.CallbackQuery):
    # await callback.message.answer(text.cheking_problem, reply_markup=kb.support_kb)
    if callback.data == "support_answer_yes":
        await callback.message.answer(text.solution_1)  # format(name=callback.from_user.full_name)
    elif callback.data == "support_answer_no":
        await callback.message.answer(text.solution_2)


@router.message(Command("contacts"))
@router.message(F.text == "menu")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
@router.message(F.text == "support")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)

# @router.callback_query()
# async def callback_handler(callback: types.CallbackQuery):
#     if callback.data == "support":
#         await callback.message.answer(text.cheking_problem, reply_markup=kb.support_kb)


# @router.message(Command("support"))
# async def support(msg: Message):
#     await msg.answer(text.cheking_problem, reply_markup=kb.support_kb)
