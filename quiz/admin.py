"""Admin configuration for the LitQuiz application."""

from django.contrib import admin

from .models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Admin settings for the Question model."""

    list_display = ('id', 'text', 'category', 'correct_answer')
    list_filter = ('category',)
    search_fields = ('text', 'explanation')
    