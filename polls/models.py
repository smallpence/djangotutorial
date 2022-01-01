"modelling for polls app"
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    "model for a question, with some text & date of publication"
    text = models.CharField(max_length=200, verbose_name='question text')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return str(self.text)

    def was_published_recently(self):
        "returns true if this question was published today"
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    "model for a choice for a question, and counts some amount of votes for it"
    question = models.ForeignKey(Question, models.CASCADE)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.text)
