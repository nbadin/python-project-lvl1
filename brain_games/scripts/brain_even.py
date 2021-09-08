#!/usr/bin/env python
from brain_games.scripts.brain_games import main as greeting
import random
import prompt


def is_even(num):
    return num % 2 == 0


def generate_question_and_answer():
    question = random.randint(1, 1000)
    answer = 'yes' if is_even(question) else 'no'
    return(question, answer)


def main():
    name = greeting()
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    print(rules)
    for i in range(0, 3):
        (questoin, answer) = generate_question_and_answer()
        print('Question: {}'.format(questoin))
        user_answer = prompt.string('Your answer: ')
        if (user_answer != answer):
            print("'{}' is wrong answer ;(. \
                Correct answer was '{}'".format(user_answer, answer))
            print("Let's try again, {}!".format(name))
            quit()
        print('Correct!')
    print('Congratulations, {}!'.format(name))
