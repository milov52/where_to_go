from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Place, Image

def home2(request):
    template = loader.get_template('index.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


def home(request):

    value = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [37.62, 55.793676]
                },
                "properties": {
                    "title": "«Легенды Москвы",
                    "placeId": "moscow_legends",
                    "detailsUrl": "static/places/moscow_legends.json"
                }
            },
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [37.64, 55.753676]
                },
                "properties": {
                    "title": "Крыши24.рф",
                    "placeId": "roofs24",
                    "detailsUrl": "static/places/roofs24.json"
                }
            }
        ]
    }


    context = {'value': value}
    return render(request, "index.html", context=context)