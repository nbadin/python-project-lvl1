import random


def is_prime(num):
    if num < 2:
        return False
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1
    return True


def generate_question_and_answer():
    question = random.randint(1, 113)
    answer = 'yes' if is_prime(question) else 'no'
    return (str(question), answer)
