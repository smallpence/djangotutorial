"testing for polls app"
import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question

def question_off_by(text, days):
    "create a question some amount of days ahead of behind"
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(text=text, pub_date=time)


# Create your tests here.
class QuestionModelTests(TestCase):
    "testing for anything questions related"

    def test_is_a_future_question_recent(self):
        "was_published_recently() returns false on a question with a future timestamp"

        future_time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=future_time)
        self.assertFalse(future_question.was_published_recently())

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertFalse(old_question.was_published_recently())

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertTrue(recent_question.was_published_recently())


class QuestionIndexViewTests(TestCase):
    "testing for the index web page"
    def test_index_exists(self):
        "makes sure there is a page at the index"
        response = self.client.get(reverse("polls:index"))
        self.assertIs(response.status_code, 200)
