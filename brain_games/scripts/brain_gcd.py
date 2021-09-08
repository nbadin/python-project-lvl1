#!/usr/bin/env python
from brain_games.scripts.brain_games import main as greeting
from brain_games.bin.gcd import generate_question_and_answer
from brain_games.engine import engine


def main():
    name = greeting()
    rules = 'Find the greatest common divisor of given numbers.'
    return engine(name, rules, generate_question_and_answer)
