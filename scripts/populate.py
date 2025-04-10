import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kocumai.settings')
import django
django.setup()

import random
from apps.aichatbot.models import Question, Choice
from faker import Faker

fakegen = Faker()
def populate(n=5):
    questions = []
    choices = []
    for _ in range(n):
        question_text = fakegen.sentence()
        question = Question.objects.create(question_text=question_text)
        questions.append(question)

        for _ in range(random.randint(1, 4)):
            choice_text = fakegen.word()
            choice = Choice.objects.create(
                question=question,
                choice_text=choice_text,
                votes=random.randint(0, 100)
            )
            choices.append(choice)

    return questions, choices

if __name__ == '__main__':
    n = 10  # Number of questions to create
    populate(n)
    print(f"Created {n} questions and their choices.")
