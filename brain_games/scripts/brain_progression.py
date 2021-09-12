from brain_games.scripts.brain_games import main as greeting
from brain_games.bin.progression import generate_question_and_answer
from brain_games.engine import engine


def main():
    name = greeting()
    rules = 'What number is missing in the progression?'
    return engine(name, rules, generate_question_and_answer)
