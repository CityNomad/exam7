from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView, DetailView, CreateView, DeleteView, UpdateView
from webapp.models import Poll
from webapp.forms import SearchForm, PollForm, ChoiceForm
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
