from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from poll.models import Question

# Create your views here.


def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'poll/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'poll/detail.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request_POST['choice'])
    except(keyError, Choice.DoesNotExist):
        
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect()
