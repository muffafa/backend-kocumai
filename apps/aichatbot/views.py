from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "aichatbot/index.html")

def chat(request):
    msgdict = { "msg": "Hello, world. You're at the Aichatbot chat." }
    return render(request, "aichatbot/chat.html", msgdict)