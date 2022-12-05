from django.http.response import HttpResponse
from django.template import loader


def home(request):
    template = loader.get_template('home.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
