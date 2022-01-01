"layout of the polls app"

from django.http import HttpResponse


def index(_):
    "root to ensure no root 404"
    return HttpResponse("Hello world from polls!")


def detail(_, question_id):
    "just print some information about a question"
    return HttpResponse(f"question id {question_id}")


def result(_, question_id):
    "show the current results for a question"
    return HttpResponse(f"question results for {question_id}")


def vote(_, question_id):
    "allow user to vote for a question"
    return HttpResponse(f"question voting for {question_id}")
