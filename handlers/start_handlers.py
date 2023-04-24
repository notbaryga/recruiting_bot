from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from lexicon.lexicon_ru import LEXICON_RU
from keyboards.keyboards import start_keyboard, main_hr_keyboard, main_user_keyboard
from models.base import base1


router: Router = Router()


@router.message(CommandStart())
async def start_answer(message: Message):
    base1.add_user(message.from_user.id)
    await message.answer(text=LEXICON_RU.start, reply_markup=start_keyboard)


@router.message(F.text == 'Наниматель')
async def choose_hr_role(message: Message):
    base1.add_role(message.from_user.id, 'employer')
    await message.answer(text=LEXICON_RU.role_been_chosen, reply_markup=main_hr_keyboard)


@router.message(F.text == 'Соискатель')
async def choose_hr_role(message: Message):
    base1.add_role(message.from_user.id, 'applicant')
    await message.answer(text=LEXICON_RU.role_been_chosen, reply_markup=main_user_keyboard)


@router.message()
async def send_answer(message: Message):
    await message.answer(text=LEXICON_RU.sorry_choose_role, reply_markup=start_keyboard)
