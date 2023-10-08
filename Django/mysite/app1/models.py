
from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Contact(models.Model):
    contact_name = models.CharField(max_length=255, unique=True)
    contact_mailaddress = models.EmailField(max_length=255)
    contact_subject = models.CharField(max_length=255, unique=True)
    contact_message = models.TextField()
    contact_time = models.DateTimeField()

    
