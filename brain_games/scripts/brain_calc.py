#!/usr/bin/env python
from brain_games.scripts.brain_games import main as greeting
from brain_games.bin.calc import generate_question_and_answer
from brain_games.engine import engine


def main():
    name = greeting()
    rules = 'Hello, Sam!\
    What is the result of the expression?'
    return engine(name, rules, generate_question_and_answer)
