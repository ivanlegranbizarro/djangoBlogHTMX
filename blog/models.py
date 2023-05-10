from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    autor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts", null=True, blank=True
    )
    subtitulo = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    contenido = models.TextField(max_length=500, validators=[MinLengthValidator(10)])
    publicacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-publicacion"]

    def __str__(self):
        return self.title
