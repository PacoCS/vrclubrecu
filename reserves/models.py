import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Sala(models.Model):
    sala_text = models.CharField(max_length=200)
    aforo = models.IntegerField(default=1)

    def __str__(self):
        return self.sala_text

class Material(models.Model):
    sala_f = models.ForeignKey(Sala, on_delete=models.CASCADE)
    material_text = models.CharField(max_length=200)

    def __str__(self):
        return self.material_text


class Reserva(models.Model):
    material = models.ManyToManyField(Material)
    usuario_f = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField('data reserva')

    def show_material(self):
        s=""
        for mat in self.material.all():
            s += mat.material_text + ","
        return s



    def was_published_recently(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)