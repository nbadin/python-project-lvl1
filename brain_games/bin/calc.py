import random


def generate_question_and_answer():
    first_num = random.randint(1, 100)
    second_num = random.randint(1, 100)
    operators = ('+', '-', '*')
    operator = operators[random.randint(0, 2)]
    if operator == '+':
        question = '{} + {}'.format(first_num, second_num)
        answer = str(first_num + second_num)
    elif operator == '-':
        question = '{} - {}'.format(first_num, second_num)
        answer = str(first_num - second_num)
    elif operator == '*':
        question = '{} * {}'.format(first_num, second_num)
        answer = str(first_num * second_num)
    return(question, answer)
