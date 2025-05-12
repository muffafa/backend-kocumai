from django.urls import path

from . import views

app_name = "basic_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("user_login/", views.user_login, name="user_login"),
    path("test/", views.TestView.as_view(), name="test"),
    path("school/", views.SchoolListView.as_view(), name="school_list"),
    path("school/<int:pk>/", views.SchoolDetailView.as_view(), name="school_detail"),
    path("create_school/", views.SchoolCreateView.as_view(), name="create_school"),
    path("update_school/<int:pk>/", views.SchoolUpdateView.as_view(), name="update_school"),
    path("delete_school/<int:pk>/", views.SchoolDeleteView.as_view(), name="delete_school"),
]