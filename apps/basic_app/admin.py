from django.contrib import admin
from .models import UserProfileInfo, School, Student

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(School)
admin.site.register(Student)