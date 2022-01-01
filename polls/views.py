"layout of the polls app"
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Question


def index(request):
    "show some recent questions at root"
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    return render(request, "polls/index.html", {
        'latest_question_list': latest_question_list
    })


def detail(request, question_id):
    "just print some information about a question"
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {
        "question": question
    })


def result(_, question_id):
    "show the current results for a question"
    return HttpResponse(f"question results for {question_id}")


def vote(_, question_id):
    "allow user to vote for a question"
    return HttpResponse(f"question voting for {question_id}")
