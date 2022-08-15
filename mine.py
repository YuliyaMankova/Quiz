import random

class Mystery:

    def __init__(self, question, answer, choices):
        self.question = question
        self.answer = answer
        self.choices = choices

    def start_quiz(self):
        print(f'Question: {self.question}')
        lst = self.choices.copy()
        lst.append(self.answer)
        random.shuffle(lst)
        for i, choice in enumerate(lst):
            print(f'{i + 1}. {choice}')
        ans = int(input('Select option: '))
        if lst[ans - 1] == self.answer:
            return True
        else:
            return False



myst = Mystery('Какое самое маленькое государство в мире?',
               'Ватикан',
               ['Монако', 'Сан-Марино', 'Лихтенштейн', 'Люксембург', 'Кипр', 'Тувалу'])

print(myst.start_quiz())