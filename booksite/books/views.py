from django.http import HttpResponse
from django.shortcuts import render, render_to_response


def search_form(request):
    return render_to_response('search_form.html')


def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted and empty form'
    return HttpResponse(message)
