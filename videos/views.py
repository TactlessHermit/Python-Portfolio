from django.views import generic
from .models import Video


# def index(request):
#     all_videos = Video.objects.all()
#     templatePath = 'all_videos.html'    #Django searches from app folder
#     context = {
#         'all_videos': all_videos,
#     }
#     return render(request, templatePath, context)
#
# def detail(request, Video_id):
#
#     try:
#         video = Video.objects.get(pk = Video_id)
#     except Video.DoesNotExist:
#         raise Http404("Video does not exist :(")
#
#     templatePath = 'video_page.html'    #Django searches from app folder
#     context = {
#         'video': video,
#     }
#     return render(request, templatePath, context)

class IndexView(generic.ListView):
    model = Video
    context_object_name = 'all_videos'
    template_name = 'videos/all_videos.html'  #Path in templates fldr


class DetailView(generic.DetailView):
    model = Video
    template_name = 'videos/video_page.html'


class AddVideo(generic.CreateView):
    model = Video
    fields = ['title', 'genre', 'video_link']
    template_name = 'videos/form/video_form.html'


class DeleteVideo(generic.DeleteView):
    model = Video
    template_name = 'videos/form/video_confirm_delete.html'
    success_url = '/videos/'