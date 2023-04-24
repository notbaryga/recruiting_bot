from dataclasses import dataclass


@dataclass
class LEXICON_RU:
    #общее
    start = 'Привет! Я - бот для поиска работы. Пожалуйста, выбери свою роль'
    sorry_choose_role = 'Прости, я тебя не понимаю. Пожалуйста, выбери роль!'
    choose_role = 'Выберите роль'
    role_been_chosen = 'Поздравляем! Роль была успешно выбрана'
    role_hr = 'Наниматель'
    role_user = 'Соискатель'
    see_vacancies = 'Смотреть вакансии'
    sorry = 'Простите, я вас не понимаю. Напишите /help для списка команд'

    #наниматель
    see_responses = 'Смотреть отклики'
    my_vacancies = 'Мои вакансии'
    delete = 'Удалить'

    #соискатель
    response = 'Откликнуться'