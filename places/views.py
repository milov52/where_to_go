from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Image, Place


def get_index_page(request):
    places = Place.objects.all()
    value = {"type": "FeatureCollection", "features": []}

    for place in places:
        details = reverse("places:api", kwargs={"place_id": place.pk})
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.langitude, place.latitude],
            },
            "properties": {
                "title": place.title,
                "detailsUrl": details,
            },
        }
        value["features"].append(feature)

    context = {"value": value}
    return render(request, "index.html", context=context)


def get_api(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    img = [image.image.url for image in place.images.all()]

    selected_place = {
        "title": place.title,
        "imgs": img,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": [place.langitude, place.latitude],
    }

    return JsonResponse(
        selected_place,
        json_dumps_params={"ensure_ascii": False},
    )
