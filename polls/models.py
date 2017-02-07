
from django.db import models
from django.utils import timezone

from antidote.model import BaseModel 

# Create your models here.


class Question(BaseModel):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
    	return self.question_text[:50] + "..."


class Choice(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
    	return self.choice_text[:50]