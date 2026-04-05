from django.contrib import admin
from django.urls import path

from quiz.views import (
    create_question,
    delete_question,
    home,
    question_detail,
    question_list,
    quiz_view,
    update_question,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('questions/', question_list, name='question_list'),
    path('questions/add/', create_question, name='create_question'),
    path('questions/<int:pk>/', question_detail, name='question_detail'),
    path('questions/<int:pk>/edit/', update_question, name='update_question'),
    path('questions/<int:pk>/delete/', delete_question, name='delete_question'),
    path('quiz/', quiz_view, name='quiz'),
]