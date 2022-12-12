from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Place


def get_index_page(request):
    places = Place.objects.all()
    value = {"type": "FeatureCollection", "features": []}

    for place in places:
        detail_info = reverse("places:api", kwargs={"place_id": place.pk})
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude],
            },
            "properties": {
                "title": place.title,
                "detailsUrl": detail_info,
            },
        }
        value["features"].append(feature)
    print(value)
    return render(request, "index.html", {"value": value})


def get_detail_info(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    img = [image.image.url for image in place.images.all()]

    selected_place = {
        "title": place.title,
        "imgs": img,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": [place.longitude, place.latitude],
    }

    return JsonResponse(
        selected_place,
        json_dumps_params={"ensure_ascii": False},
    )
