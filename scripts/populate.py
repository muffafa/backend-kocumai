import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kocumai.settings')
import django
django.setup()

import random
from apps.aichatbot.models import Question, Choice, User
from faker import Faker

fakegen = Faker()
def populate(n=5):
    questions = []
    choices = []
    users = []
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

    for _ in range(n):
        first_name = fakegen.first_name()
        last_name = fakegen.last_name()
        email = fakegen.email()
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        users.append(user)

    return questions, choices, users
# This script populates the database with fake data for testing purposes.

if __name__ == '__main__':
    n = 10  # Number of questions to create
    populate(n)
    print(f"Created {n} questions and their choices.")
    print(f"Created {n} users.")
