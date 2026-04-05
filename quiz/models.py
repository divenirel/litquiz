from django.db import models


class Question(models.Model):
    CATEGORY_CHOICES = [
        ('author', 'Автор'),
        ('work', 'Произведение'),
        ('image', 'По картинке'),
    ]

    text = models.TextField(verbose_name='Текст вопроса')
    image = models.URLField(blank=True, null=True, verbose_name='Ссылка на изображение')

    option_a = models.CharField(max_length=255, verbose_name='Вариант A')
    option_b = models.CharField(max_length=255, verbose_name='Вариант B')
    option_c = models.CharField(max_length=255, verbose_name='Вариант C')
    option_d = models.CharField(max_length=255, verbose_name='Вариант D')

    correct_answer = models.CharField(max_length=1, verbose_name='Правильный ответ (A/B/C/D)')

    explanation = models.TextField(blank=True, verbose_name='Пояснение')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='author')

    def __str__(self):
        return self.text