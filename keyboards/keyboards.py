from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

from lexicon.lexicon_ru import LEXICON_RU

#стартовая клавиатура с выбором роли
btn_hr: KeyboardButton = KeyboardButton(text=LEXICON_RU.role_hr)
btn_user: KeyboardButton = KeyboardButton(text=LEXICON_RU.role_user)
start_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[btn_hr, btn_user]],
                                    resize_keyboard=True,
                                    input_field_placeholder=LEXICON_RU.choose_role)

#основная клавиатура нанимателя
btn_1: KeyboardButton = KeyboardButton(text=LEXICON_RU.my_vacancies)
btn_2: KeyboardButton = KeyboardButton(text=LEXICON_RU.see_responses)
main_hr_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[btn_1, btn_2]],
                                    resize_keyboard=True)


#основная клавиатура соискателя
btn_1: KeyboardButton = KeyboardButton(text=LEXICON_RU.see_vacancies)
main_user_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[btn_1]],
                                    resize_keyboard=True)