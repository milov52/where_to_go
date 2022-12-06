from django.shortcuts import render

from .models import Place


def home(request):
    places = Place.objects.all()

    value = {"type": "FeatureCollection", "features": []}

    for place in places:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.coord_lng, place.coord_lat],
            },
            "properties": {
                "title": place.title,
                "placeId": place.placeId,
                "detailsUrl": "static/places/moscow_legends.json"
                if place.placeId == "moscow_legends"
                else "static/places/roofs24.json",
            },
        }
        value["features"].append(feature)

    context = {"value": value}
    return render(request, "index.html", context=context)
