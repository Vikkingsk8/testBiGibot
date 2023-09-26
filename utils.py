# import text
# from aiogram import Router, types
# import keyboard as kb
#
# router = Router()
#
#
# @router.callback_query()
# async def answer_1(callback_query: types.CallbackQuery):
#     await callback_query.answer(reply_markup=kb.)


# @router.message(Command("support"))
# async def support(msg: Message):
#     await msg.answer(text.cheking_problem, reply_markup=kb.support_kb)
#     #await callback.message.answer(text.cheking_problem, reply_markup=kb.support_kb)
#
#
# @router.callback_query()
# async def support_handler(callback: types.CallbackQuery):
#     if callback.data == "support_answer_yes":
#         await callback.message.answer(text.solution_1)  # format(name=callback.from_user.full_name)
#     elif callback.data == "support_answer_no":
#         await callback.message.answer(text.solution_2)