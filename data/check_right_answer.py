from random import choice


def check(text: str, right: str):
    if text == right:
        return True
    else:
        return False


def answers(type_of_answer: str):
    answers = []
    if type_of_answer == 'wrong':
        answers = ['неа, еще попробуй😡', 'мимо🤔', 'не гадай а..🥵']
    elif type_of_answer == 'good':
        answers = ['Умочка❤️ некст..', 'Правильно!😍 Идем дальше...', 'Подарок уже близко🥰 Дальше...']

    return choice(answers)