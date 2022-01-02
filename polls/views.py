"layout of the polls app"
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Question, Choice


class IndexView(generic.ListView):
    "auto generated view for page root, displaying latest 5 qs"
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        "yield the context object (5 latest questions)"
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    "auto generated view detailing a question"
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    "auto generated view detailing a question"
    model = Question
    template_name = "polls/results.html"


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
