from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("chat/", views.chat, name="chat"),
    path("question/", views.question, name="question"),
    path("user/", views.user, name="user"),
    path("register/", views.register, name="register"),
]