from django.urls import path
from webapp.views import IndexView, PollView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    # path('projects/', RedirectView.as_view(pattern_name="home")),
    # path('projects/add/', CreateProject.as_view(), name="create_project"),
    path('poll/<int:pk>/', PollView.as_view(), name="poll_view"),
    # path('task/<int:pk>/update/', UpdateTask.as_view(), name="update_task"),
    # path('task/<int:pk>/', TaskView.as_view(), name="task_view"),
    # path('task/<int:pk>/delete/', DeleteTask.as_view(), name="delete_task"),
    # path('project/<int:pk>/task/add/', CreateTask.as_view(), name="create_task"),
    # path('projects/<int:pk>/update/', UpdateProject.as_view(), name='update_project'),
    # path('projects/<int:pk>/delete/', DeleteProject.as_view(), name='delete_project'),

]