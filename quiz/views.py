from django.shortcuts import render
from .models import Question


def home(request):
    return render(request, 'home.html')


def question_list(request):
    questions = Question.objects.all().order_by('id')
    return render(request, 'question_list.html', {'questions': questions})