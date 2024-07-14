from django.urls import include, path
from . import views

app_name = 'designs'

urlpatterns = [
    # /designs/
    path('', views.AllDesigns.as_view(), name="all_designs"),

    # /designs/{id}/
    path('<int:pk>/', views.DesignDetails.as_view(), name="design_page"),

    # /designs/add/
    path('add/', views.AddDesign.as_view(), name="add_design"),

    # /designs/delete/
    path('<int:pk>/delete/', views.DeleteDesign.as_view(), name="delete_design"),
]