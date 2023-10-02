from aiogram import F, Router, types, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import asyncio

import keyboard as kb
import text

router = Router()


# Стартовый  хэндлер
@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)


@router.callback_query(F.data.startswith('tariffs'))
async def tariffs_handler(callback: types.CallbackQuery):
    await callback.message.answer(text.tariffs, reply_markup=kb.tariffs_kb)


@router.callback_query(F.data.startswith('payment'))
async def payment_handler(callback: types.callback_query):
    await callback.message.answer(text.payment, reply_markup=kb.payment_kb)


@router.callback_query(F.data.startswith('support'))
async def support_handler_answer(callback: types.CallbackQuery):
    await callback.message.answer(text.cheking_problem)


# @router.callback_query(F.data.startswith('support_answer_yes'))
# async def support_handler(callback: types.CallbackQuery):
#     if callback.data == "support_answer_yes":
#         await callback.message.answer(text.solution_1)  # format(name=callback.from_user.full_name)
#     elif callback.data == "support_answer_no":
#         await callback.message.answer(text.solution_2)


@router.callback_query(F.data.startswith('contacts'))
async def contacts_handler(callback: types.CallbackQuery):
    await callback.message.answer(text.contact)


@router.callback_query(F.data.startswith('other_questions'))
async def other_questions_handler(callback: types.CallbackQuery):
    await callback.message.answer(text.other_questions)


@router.message(F.text == "menu")
@router.message(F.text == "Выйти в меню")
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
