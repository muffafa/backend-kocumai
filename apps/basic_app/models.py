from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class UserProfileInfo(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)

   portfolio_site = models.URLField(blank=True)
   profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
   
   def __str__(self):
        return self.user.username
   

class School(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('basic_app:school_detail', kwargs={'pk': self.pk})
    
class Student(models.Model):
      first_name = models.CharField(max_length=50)
      last_name = models.CharField(max_length=50)
      date_of_birth = models.DateField()
      school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')
   
      def __str__(self):
         return f"{self.first_name} {self.last_name}"