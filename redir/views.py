from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponseRedirect

from .utils import code_generator
from .models import ShortURL


def home(request):
    return render(request, 'redir/home.html')


def shorten(request):
    original_url = request.GET['originalurl']
    uri = code_generator()
    obj = ShortURL(url=original_url, short_url=uri, created_date=timezone.now())
    obj.save()
    # TODO add error message for this case
    '''
        if obj.clean():
            obj.save()
            return render(request, 'redir/shorten.html',
                          {'original': obj.url, 'shorten': request.get_host() + '/' + uri, 'date': obj.created_date})
        else:

            return render(request, 'redir/home.html')
            '''
    return render(request, 'redir/shorten.html',
                  {'original': obj.url, 'shorten': request.get_host() + '/' + uri, 'date': obj.created_date})




def redirect_to_original(request, short_url=None):
    obj = get_object_or_404(ShortURL, short_url=short_url)
    obj.counter += 1
    obj.save()
    return HttpResponseRedirect(obj.url)
