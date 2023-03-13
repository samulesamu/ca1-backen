from django.db import models
from django.contrib.auth.models import User




from django.contrib.auth import get_user
# Create your models here.


class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    nb_notes = models.IntegerField(default=0)

    def __str__(self):
        return self.subject_name

class Notes(models.Model):
    name = models.CharField(max_length=100, default='')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    file = models.FileField(upload_to='./notes/', default='')
    date = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)




    def __str__(self):
        return self.name
