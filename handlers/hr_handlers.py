from aiogram import Router, F
from aiogram.filters import BaseFilter
from aiogram.types import Message

from lexicon.lexicon_ru import LEXICON_RU
#from filters.hr_filter import IsHR

from models.base import base

router: Router = Router()
router.message.filter(base.get_user(F.text) is not None)

@router.message(F.text == LEXICON_RU.see_responses)
async def choose_hr_role(message: Message):
    #await message.answer(text=LEXICON_RU.role_been_chosen, reply_markup=main_hr_keyboard)
    await message.answer('Вот ваши отклики:') #заменить


@router.message(F.text == LEXICON_RU.my_vacancies)
async def choose_hr_role(message: Message):
    #await message.answer(text=LEXICON_RU.role_been_chosen, reply_markup=main_user_keyboard)
    await message.answer('Вот ваши вакансии:')  # заменить

@router.message()
async def send_answer(message: Message):
    await message.answer(text=LEXICON_RU.sorry)
