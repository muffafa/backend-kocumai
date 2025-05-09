from django.shortcuts import render
from django.http import HttpResponse
from apps.aichatbot.models import Question, Choice, User
from .forms import NewUserForm

# Create your views here.
def index(request):
    return render(request, "aichatbot/index.html")

def chat(request):
    msgdict = { "msg": "Hello, world. You're at the Aichatbot chat." }
    return render(request, "aichatbot/chat.html", msgdict)

def question(request):
    question_list = Question.objects.all()
 
    choice_list = Choice.objects.all()
    context = {
        'question_list': question_list,
        'choice_list': choice_list,
    }
   
    return render(request, "aichatbot/question.html", context)

def user(request):
    user_list = User.objects.all()
    context = {
        'user_list': user_list,
    }
    return render(request, "aichatbot/user.html", context)

def register(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
        else:
            print("Form is not valid")

    return render(request, "aichatbot/register.html" , {"form": form})