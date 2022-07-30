from django.urls import path
from webapp.views import IndexView, PollView, CreatePoll, UpdatePoll

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    # path('projects/', RedirectView.as_view(pattern_name="home")),
    path('polls/add/', CreatePoll.as_view(), name="create_poll"),
    path('poll/<int:pk>/', PollView.as_view(), name="poll_view"),
    path('polls/<int:pk>/update/', UpdatePoll.as_view(), name='update_poll'),
    # path('task/<int:pk>/update/', UpdateTask.as_view(), name="update_task"),
    # path('task/<int:pk>/', TaskView.as_view(), name="task_view"),
    # path('task/<int:pk>/delete/', DeleteTask.as_view(), name="delete_task"),
    # path('project/<int:pk>/task/add/', CreateTask.as_view(), name="create_task"),

    # path('projects/<int:pk>/delete/', DeleteProject.as_view(), name='delete_project'),

]