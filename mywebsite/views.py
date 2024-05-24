# from django.http import HttpResponse
from django.shortcuts import render


# method view
def index(request):
    context = {
        'page_title':'Home',
    }
    return render(request, 'index.html', context)
