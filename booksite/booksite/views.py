from django.shortcuts import render_to_response, render
from django.template.loader import get_template
from django.template import Context
from django.http import Http404, HttpResponse
import datetime
# from django.utils import timezone


def hello(request):
    return HttpResponse("Hello world")


def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('hours_ahead.html', {'hour_offset': offset, 'next_time': dt})
    # html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    # return HttpResponse(html)


def meta_detail(request):
    """Display META values"""
    # path get_host get_full_path is_secure
    values = request.META.items()
    # create list of formatted strings
    meta_items = []
    # now append other HttpRequest methods
    meta_items.append("{}: {}".format('request.path', request.path))
    meta_items.append("{}: {}".format('request.get_host()', request.get_host()))
    meta_items.append("{}: {}".format('request.get_full_path()', request.get_full_path()))
    meta_items.append("{}: {}".format('request.is_secure()', request.is_secure()))
    for value in values:
        meta_items.append("{}: {}".format(value[0], value[1]))
    return render(request, 'meta_detail.html', {'meta_items': meta_items})
