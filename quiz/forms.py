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

    def clean_correct_answer(self):
        answer = self.cleaned_data.get('correct_answer')
        if answer not in ['A', 'B', 'C', 'D']:
            raise forms.ValidationError('Ответ должен быть A, B, C или D')
        return answer