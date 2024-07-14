from django.urls import path
from . import views

app_name = 'videos'

urlpatterns = [
    # '/videos/'
    path('', views.IndexView.as_view(), name='index'),

    # '/videos/id/'   where id = 1,2,3,4,5,etc.
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # '/videos/add/'
    path('add/', views.AddVideo.as_view(), name='add-video'),

    # '/videos/id/delete/'   where id = 1,2,3,4,5,etc.
    path('<int:pk>/delete/', views.DeleteVideo.as_view(), name='del-video'),
]