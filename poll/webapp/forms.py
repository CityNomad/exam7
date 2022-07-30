from django import forms
from django.forms import widgets
from webapp.models import Poll, Choice

class PollForm(forms.ModelForm):

    class Meta:
        model = Poll
        fields = ["question"]
        widgets = {
            "question": widgets.Textarea(attrs={"placeholder": "введите вопрос"}),
        }

class SearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label='Найти')

class ChoiceForm(forms.ModelForm):

    class Meta:
        model = Choice
        fields = ["text"]
        widgets = {
            "text": widgets.Textarea(attrs={"placeholder": "введите ответ"}),
        }