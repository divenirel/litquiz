from django import forms

from .models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'text',
            'image',
            'option_a',
            'option_b',
            'option_c',
            'option_d',
            'correct_answer',
            'explanation',
            'category',
        ]
        labels = {
            'text': 'Текст вопроса',
            'image': 'Ссылка на изображение',
            'option_a': 'Вариант A',
            'option_b': 'Вариант B',
            'option_c': 'Вариант C',
            'option_d': 'Вариант D',
            'correct_answer': 'Правильный ответ',
            'explanation': 'Пояснение',
            'category': 'Категория',
        }
        help_texts = {
            'image': 'Поле необязательное. Можно вставить ссылку на изображение.',
            'correct_answer': 'Введите одну букву: A, B, C или D.',
            'explanation': 'Поле необязательное. Можно пояснить, почему ответ правильный.',
        }
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Введите текст вопроса',
            }),
            'image': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://example.com/image.jpg',
            }),
            'option_a': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите вариант A',
            }),
            'option_b': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите вариант B',
            }),
            'option_c': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите вариант C',
            }),
            'option_d': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите вариант D',
            }),
            'correct_answer': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например: A',
            }),
            'explanation': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Введите пояснение к ответу',
            }),
            'category': forms.Select(attrs={
                'class': 'form-select',
            }),
        }

    def clean_text(self):
        text = self.cleaned_data.get('text', '').strip()

        if len(text) < 10:
            raise forms.ValidationError('Текст вопроса должен содержать минимум 10 символов.')

        return text

    def clean_correct_answer(self):
        answer = self.cleaned_data.get('correct_answer', '').strip().upper()

        if answer not in ['A', 'B', 'C', 'D']:
            raise forms.ValidationError('Введите A, B, C или D.')

        return answer

    def clean(self):
        cleaned_data = super().clean()

        option_a = cleaned_data.get('option_a', '').strip()
        option_b = cleaned_data.get('option_b', '').strip()
        option_c = cleaned_data.get('option_c', '').strip()
        option_d = cleaned_data.get('option_d', '').strip()

        options = [option_a, option_b, option_c, option_d]
        filled_options = [option for option in options if option]

        if len(filled_options) != len(set(filled_options)):
            raise forms.ValidationError('Варианты ответа не должны повторяться.')

        return cleaned_data