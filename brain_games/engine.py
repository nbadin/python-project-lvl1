import prompt


def engine(name, rules, generate_task):
    print(rules)
    for i in range(0, 3):
        (questoin, answer) = generate_task()
        print('Question: {}'.format(questoin))
        user_answer = prompt.string('Your answer: ')
        if (user_answer != answer):
            print("'{}' is wrong answer ;(. \
            Correct answer was '{}'".format(user_answer, answer))
            print("Let's try again, {}!".format(name))
            quit()
        print('Correct!')
    print('Congratulations, {}!'.format(name))
