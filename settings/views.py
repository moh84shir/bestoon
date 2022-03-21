from django.shortcuts import render
from .models import SiteSetting


def index(request):
    setting_obj = SiteSetting.objects.last()
    if setting_obj is None:
        SiteSetting.objects.create()
            
    user = request.user
    if user.is_anonymous:
        user = None
    context = {}
    context['user'] = user
    context['title'] = setting_obj.title
    context['about'] = setting_obj.about
    context['github_addr'] = setting_obj.github_addr
    
    return render(request, 'index.html', context)

