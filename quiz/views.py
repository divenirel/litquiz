from django.shortcuts import get_object_or_404, redirect, render

from .forms import QuestionForm
from .models import Question


def home(request):
    return render(request, 'home.html')


def question_list(request):
    questions = Question.objects.all().order_by('id')
    return render(request, 'question_list.html', {'questions': questions})


def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('question_list')
    else:
        form = QuestionForm()

    return render(request, 'question_form.html', {'form': form, 'page_title': 'Добавить вопрос'})


def update_question(request, pk):
    question = get_object_or_404(Question, pk=pk)

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('question_list')
    else:
        form = QuestionForm(instance=question)

    return render(request, 'question_form.html', {'form': form, 'page_title': 'Редактировать вопрос'})