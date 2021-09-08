import random


def get_gcd(a, b):
    divider = min(a, b)
    while (divider > 0):
        if a % divider == 0 and b % divider == 0:
            return divider
        divider -= 1


def generate_question_and_answer():
    first_num = random.randint(1, 100)
    second_num = random.randint(1, 100)
    question = '{} {}'.format(first_num, second_num)
    answer = str(get_gcd(first_num, second_num))
    return (question, answer)
