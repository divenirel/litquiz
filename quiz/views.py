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

    return render(
        request,
        'question_form.html',
        {
            'form': form,
            'page_title': 'Добавить вопрос',
        }
    )


def update_question(request, pk):
    question = get_object_or_404(Question, pk=pk)

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('question_list')
    else:
        form = QuestionForm(instance=question)

    return render(
        request,
        'question_form.html',
        {
            'form': form,
            'page_title': 'Редактировать вопрос',
        }
    )


def delete_question(request, pk):
    question = get_object_or_404(Question, pk=pk)

    if request.method == 'POST':
        question.delete()
        return redirect('question_list')

    return render(
        request,
        'question_confirm_delete.html',
        {
            'question': question,
            'page_title': 'Удалить вопрос',
        }
    )


def quiz_view(request):
    questions = Question.objects.all().order_by('id')

    if not questions.exists():
        return render(
            request,
            'quiz.html',
            {
                'questions': questions,
                'page_title': 'Литературный квиз',
            }
        )

    if request.method == 'POST':
        total_questions = questions.count()
        correct_count = 0
        answers = []

        for question in questions:
            user_answer = request.POST.get(f'question_{question.id}', '')
            correct_answer = question.correct_answer.upper()
            is_correct = user_answer == correct_answer

            if is_correct:
                correct_count += 1

            answers.append(
                {
                    'question': question,
                    'user_answer': user_answer,
                    'correct_answer': correct_answer,
                    'is_correct': is_correct,
                }
            )

        return render(
            request,
            'quiz_result.html',
            {
                'page_title': 'Результат квиза',
                'total_questions': total_questions,
                'correct_count': correct_count,
                'answers': answers,
            }
        )

    return render(
        request,
        'quiz.html',
        {
            'questions': questions,
            'page_title': 'Литературный квиз',
        }
    )