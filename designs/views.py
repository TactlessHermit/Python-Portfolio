from django.shortcuts import render
from django.views import generic
from .models import Designs


# Create your views here.
class AllDesigns(generic.ListView):
    model = Designs
    context_object_name = "all_designs"
    template_name = "webpages/all_designs.html"


class DesignDetails(generic.DetailView):
    model = Designs
    context_object_name = "design"
    template_name = "webpages/design_page.html"

class AddDesign(generic.CreateView):
    model = Designs
    fields = ['name','software','description']
    template_name = "forms/create_form.html"

class DeleteDesign(generic.DeleteView):
    model = Designs
    template_name = 'forms/confirm_delete.html'
    success_url = '/designs/'
