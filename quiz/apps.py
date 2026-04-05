"""Application configuration for LitQuiz."""

from django.apps import AppConfig


class QuizConfig(AppConfig):
    """Configuration for the quiz application."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quiz'
    