from django.db import models

# Create your models here.

class Login(models.Model):
    check_mail = models.CharField(max_length=5)
    email = models.CharField(max_length=50)
    token = models.CharField(max_length=50)
    delete_yn = models.CharField(max_length=1)
    start_dt = models.DateField()
    end_dt = models.DateField()
    last_dt = models.DateField()
    