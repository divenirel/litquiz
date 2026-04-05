from django.contrib import admin
from django.urls import path

from quiz.views import create_question, delete_question, home, question_list, update_question

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('questions/', question_list, name='question_list'),
    path('questions/add/', create_question, name='create_question'),
    path('questions/<int:pk>/edit/', update_question, name='update_question'),
    path('questions/<int:pk>/delete/', delete_question, name='delete_question'),
]