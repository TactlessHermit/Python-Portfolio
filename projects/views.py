from django.views import generic
from .models import Projects


# Create your views here.
# Shows all projects
class IndexView(generic.ListView):
    model = Projects
    context_object_name = 'projects_list'
    template_name = 'webpages/all_projects.html'


class ProjectDetailView(generic.DetailView):
    model = Projects
    context_object_name = 'project'
    template_name = 'webpages/project_page.html'


class AddProjectView(generic.CreateView):
    model = Projects
    template_name = 'forms/create_form.html'
    fields = ['project_name', 'language', 'framework', 'description', 'project_link']
