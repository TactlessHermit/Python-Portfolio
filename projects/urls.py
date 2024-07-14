from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    # '/projects/'
    path('', views.IndexView.as_view(), name='all-projects'),

    # '/projects/id/
    path('<int:pk>/', views.ProjectDetailView.as_view(), name='project-page'),

    # '/projects/add/'
    path('add/', views.AddProjectView.as_view(), name='add-project'),
]
