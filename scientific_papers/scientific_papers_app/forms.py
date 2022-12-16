from .models import Paper
from django.forms import ModelForm, TextInput, Textarea, NumberInput


class PaperForm(ModelForm):
    class Meta:
        model = Paper
        fields = ['title', 'author', 'text', 'published', 'citations_count']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть назву'
            }),
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть автора'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть короткий опис'
            }),
            'published': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть рік видання'
            }),
            'citations_count': NumberInput(attrs={
                'class': 'col-xs-2',
                'id': 'ex2',
                'placeholder': 'Введіть кількість цитувань'
            })
        }