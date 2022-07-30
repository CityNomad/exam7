from django import forms
from django.forms import widgets
from webapp.models import Poll

class PollForm(forms.ModelForm):

    class Meta:
        model = Poll
        fields = ["question", "created_at"]
        widgets = {
            "question": widgets.Textarea(attrs={"placeholder": "введите вопрос"}),
        }
