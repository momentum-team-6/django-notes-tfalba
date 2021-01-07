from django.db import models
from django.contrib.auth.models import AbstractUser

from django.urls import reverse

# Create your models here.


class Label(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    
    def __str__(self):
        return f'{self.name}'

class Note(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField(max_length=2000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    labels = models.ManyToManyField('Label', related_name='notes', help_text='Select any tags for this note')
    
    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('note-detail', args=[str(self.id)])

class Comment(models.Model):
    text = models.TextField(max_length=1000, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    note = models.ForeignKey(Note, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text}'


class User(AbstractUser):
    pass
