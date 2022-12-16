from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Place


def get_index_page(request):
    places = Place.objects.all()
    place_info = {"type": "FeatureCollection", "features": []}

    for place in places:
        detail_info = reverse(
            "places:detail_info", kwargs={"place_id": place.pk}
        )
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
        place_info["features"].append(feature)
    return render(request, "index.html", {"value": place_info})


def get_detail_info(request, place_id):
    place = get_object_or_404(Place, pk=place_id)

    selected_place = {
        "title": place.title,
        "imgs": [image.image.url for image in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": [place.longitude, place.latitude],
    }

    return JsonResponse(
        selected_place,
        json_dumps_params={"ensure_ascii": False},
    )
