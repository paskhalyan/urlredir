from django.shortcuts import render
from django.utils import timezone

from .utils import code_generator
from .models import ShortURL


def home(request):
    return render(request, 'redir/home.html')


def shorten(request):
    original_url = request.GET['originalurl']
    uri = code_generator()
    obj = ShortURL(url=original_url, short_url=request.get_host() + '/' + uri, created_date=timezone.now())
    obj.save()
    return render(request, 'redir/shorten.html', {'original': obj.url, 'shorten': obj.short_url, 'date': obj.created_date})


