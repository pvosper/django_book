from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import Http404, HttpResponse
import datetime
# from django.utils import timezone


def hello(request):
    return HttpResponse("Hello world")


def current_datetime(request):
    now = datetime.datetime.now()
    # now = timezone.now()  # Doesn't use settings timezone
    # t = get_template('current_datetime.html')
    # html = t.render(Context({'current_date': now}))  # Not Django 1.8+
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)
    context = {'current_date': now}
    return render(request, 'current_datetime.html', context)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)