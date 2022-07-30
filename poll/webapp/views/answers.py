from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, View
from webapp.models import Answer, Poll, Choice
from webapp.forms import PollForm, ChoiceForm
from django.urls import reverse_lazy, reverse


class CreateAnswer(TemplateView):
    template_name = "answers/answer.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        poll = get_object_or_404(Poll, pk=kwargs['pk'])
        choices = get_object_or_404(Choice, pk=kwargs['pk'])
        context['poll'] = poll
        context['choice'] = choices
        return render(request, "create_answer", context)

    def post(self, request, *args, **kwargs):
        answer = get_object_or_404(Answer, pk=kwargs['pk'])
        answer.choice = self.request.POST.get('answer')
        answer.save()
        return render(request, "poll_view")
