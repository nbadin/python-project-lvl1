from brain_games.scripts.brain_games import main as greeting
from brain_games.bin.prime import generate_question_and_answer
from brain_games.engine import engine


def main():
    name = greeting()
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    return engine(name, rules, generate_question_and_answer)
