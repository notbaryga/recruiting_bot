from aiogram import Router, F
from aiogram.types import Message

from lexicon.lexicon_ru import LEXICON_RU
from filters.hr_filter import IsHR


router: Router = Router()
router.message.filter(IsHR())

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
