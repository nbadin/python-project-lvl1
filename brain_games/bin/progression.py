import random


def generate_progression():
    progression_length = random.randint(5, 15)
    first_num = random.randint(1, 15)
    progression_step = random.randint(2, 10)
    i = 1
    progression = (first_num,)
    while i < progression_length:
        current_value = progression[len(progression) - 1] + progression_step
        progression += (current_value, )
        i += 1
    return progression


def generate_question_and_answer():
    progression = generate_progression()
    hidden_index = random.randint(0, len(progression) - 1)
    answer = str(progression[hidden_index])
    question = ''
    for item in progression:
        if item == progression[hidden_index]:
            question += '..'
        else:
            question += str(item)
        question += ' '
    return (question, answer)
