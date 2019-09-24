from django.shortcuts import get_object_or_404, render
from poll.models import Question

# Create your views here.
def index :
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = { 'latest_question_list': latest_question_list }
    return render(request, 'index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    render(request, 'poll/index.html', { 'question': question })