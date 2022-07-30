from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DeleteView, UpdateView
from webapp.models import Choice, Poll
from webapp.forms import PollForm, ChoiceForm
from django.urls import reverse_lazy, reverse

# Create your views here.

class CreateChoice(CreateView):
    model = Choice
    template_name = 'choices/create_choice.html'
    form_class = ChoiceForm

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        choice = form.save(commit=False)
        choice.poll = poll
        poll.save()
        return redirect('poll_view', pk=poll.pk)

class UpdateChoice(UpdateView):
    form_class = ChoiceForm
    template_name = "choices/update_choice.html"
    model = Choice

    def get_success_url(self):
        return reverse("poll_view", kwargs={"pk": self.object.poll.pk})
