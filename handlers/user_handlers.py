from aiogram import Router, F
from aiogram.types import Message

from lexicon.lexicon_ru import LEXICON_RU
from filters.user_filter import IsUser


router: Router = Router()
router.message.filter(IsUser)

@router.message(F.text == LEXICON_RU.see_vacancies)
async def choose_hr_role(message: Message):
    await message.answer('Вот доступные вакансии:') #заменить


@router.message()
async def send_answer(message: Message):
    await message.answer(text=LEXICON_RU.sorry)
