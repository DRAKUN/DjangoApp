from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(blank=True, null=True,max_length=200)
    status = models.CharField(default='inactive',max_length=10)
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete="CASCADE")

    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Choice(models.Model):
    question = models.ForeignKey('poll.Question', on_delete="CASCADE")
    text = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text