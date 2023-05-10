from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    autor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts", null=True, blank=True
    )
    subtitle = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    content = RichTextUploadingField()
    publication = models.DateTimeField(auto_now_add=True)
    modification = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-publication"]

    def __str__(self):
        return self.title
