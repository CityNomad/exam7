from django.urls import path
from webapp.views import IndexView, PollView, CreatePoll, UpdatePoll, DeletePoll, CreateChoice, UpdateChoice, DeleteChoice, CreateAnswer
from django.views.generic import RedirectView, TemplateView
from webapp.models import Poll


urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('polls/', RedirectView.as_view(pattern_name="index")),
    path('polls/add/', CreatePoll.as_view(), name="create_poll"),
    path('poll/<int:pk>/', PollView.as_view(), name="poll_view"),
    path('polls/<int:pk>/update/', UpdatePoll.as_view(), name='update_poll'),
    path('polls/<int:pk>/delete/', DeletePoll.as_view(), name='delete_poll'),
    path('polls/<int:pk>/choice/add/', CreateChoice.as_view(), name="create_choice"),
    path('choice/<int:pk>/update/', UpdateChoice.as_view(), name="update_choice"),
    path('choice/<int:pk>/delete/', DeleteChoice.as_view(), name="delete_choice"),
    path('answer/<int:pk>/', TemplateView.as_view(template_name='answers/answer.html'), name='create_answer'),



]