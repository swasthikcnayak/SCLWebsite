from django.db import models

# Create your models here.
from django.urls import reverse


class Teams(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='teams', default='default.jpg')
    problem_statement = models.TextField()
    presentation = models.FileField(upload_to="presentations/",null=True)
    cookies = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('team', kwargs={'team_id': self.id})
