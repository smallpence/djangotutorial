"layout of the polls app"
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question, Choice


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


def result(request, question_id):
    "show the current results for a question"
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {
        'question': question
    })


def vote(request, question_id):
    "allow user to vote for a question"
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Invalid choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
