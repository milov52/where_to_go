from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Image, Place


def home(request):
    places = Place.objects.all()
    value = {"type": "FeatureCollection", "features": []}

    for place in places:
        details = reverse("places:api", kwargs={"place_id": place.pk})
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.coord_lng, place.coord_lat],
            },
            "properties": {
                "title": place.title,
                "placeId": place.placeId,
                "detailsUrl": details,
            },
        }
        value["features"].append(feature)

    context = {"value": value}
    return render(request, "index.html", context=context)


def api(request, place_id):
    place = get_object_or_404(Place, pk=place_id)

    images = Image.objects.filter(places=place_id)
    img = []
    for image in images:
        img.append(str(image.place_image.url))

    data = {
        "title": place.title,
        "imgs": img,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": [place.coord_lng, place.coord_lat],
    }

    return JsonResponse(
        data,
        safe=False,
        json_dumps_params={"ensure_ascii": False, "indent": 2},
    )
