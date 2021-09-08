import random


def is_even(num):
    return num % 2 == 0


def generate_question_and_answer():
    question = random.randint(1, 1000)
    answer = 'yes' if is_even(question) else 'no'
    return(question, answer)
