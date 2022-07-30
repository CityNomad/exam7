from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from webapp.models import Poll
from webapp.forms import SearchForm, PollForm, ChoiceForm
from django.urls import reverse_lazy
# Create your views here.

class IndexView(ListView):
    model = Poll
    template_name = "polls/index.html"
    context_object_name = "polls"
    paginate_by = 5

    def get_queryset(self):
        return Poll.objects.all().order_by('-created_at')

class PollView(DetailView):
    template_name = "polls/poll_view.html"
    model = Poll

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['choices'] = self.object.choices.order_by("id")
        context['counts'] = self.object.choices.count()
        return context

class CreatePoll(CreateView):
    form_class = PollForm
    template_name = "polls/create_poll.html"

    def form_valid(self, form):
        poll = form.save(commit=False)
        poll.save()
        form.save_m2m()
        return redirect("poll_view", pk=poll.pk)

class UpdatePoll(UpdateView):
    model = Poll
    template_name = 'polls/update_poll.html'
    form_class = PollForm
    context_object_name = 'poll'

class DeletePoll(DeleteView):
    model = Poll
    context_object_name = 'poll'
    template_name = 'polls/delete_poll.html'
    success_url = reverse_lazy('index')