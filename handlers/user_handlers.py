from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from lexicon.lexicon_ru import LEXICON_RU
from filters.user_filter import IsUser

from models.base import base1
from keyboards.keyboards import main_hr_keyboard

router: Router = Router()
router.message.filter(IsUser())

@router.message(Command(commands=['changerole']))
async def changerole(message: Message):
    base1.add_role(message.from_user.id, 'employer')
    await message.answer(LEXICON_RU.role_changed, reply_markup=main_hr_keyboard)

@router.message(F.text == LEXICON_RU.see_vacancies)
async def choose_hr_role(message: Message):
    await message.answer('Вот доступные вакансии:') #заменить


@router.message()
async def send_answer(message: Message):
    await message.answer(text=LEXICON_RU.sorry)
