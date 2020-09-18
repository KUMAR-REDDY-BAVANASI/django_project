from django.db import models
from .validators import validate_file_size


class StudentProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=100)
    location = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/')
    resume = models.FileField(upload_to='files/',validators=[validate_file_size])