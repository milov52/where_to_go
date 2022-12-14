from urllib.parse import urlparse

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Image, Place


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("place_url", nargs="+", type=str)

    def handle(self, *args, **options):
        for place_url in options["place_url"]:
            response = requests.get(place_url)

            place_info = response.json()
            if "error" in place_info:
                raise requests.exceptions.HTTPError(place_info["error"])

            place, is_place_created = Place.objects.get_or_create(
                title=place_info["title"],
                longitude=place_info["coordinates"]["lng"],
                latitude=place_info["coordinates"]["lat"],
                defaults={
                    "description_short": place_info.get(
                        "description_short", ""
                    ),
                    "description_long": place_info.get("description_long", ""),
                },
            )

            if is_place_created:
                images = place_info.get("imgs", "")
                for position, file_name in enumerate(images):
                    image_name = urlparse(file_name).path.split("/")[-1]

                    image_content = response.content
                    content_file = ContentFile(image_content, name=image_name)
                    Image.objects.create(
                        places=place, image=content_file, position=position
                    )
