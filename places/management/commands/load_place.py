from urllib.parse import urlparse

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Image, Place


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("place_url", nargs="+", type=str)

    def create_image(self, place_info, place):
        images = place_info.get("imgs", [])
        for position, image_url in enumerate(images):
            response = requests.get(image_url)

            response.raise_for_status()
            image_name = urlparse(image_url).path.split("/")[-1]
            content_file = ContentFile(response.content, name=image_name)
            Image.objects.create(
                places=place, image=content_file, position=position
            )

    def handle(self, *args, **options):
        for place_url in options["place_url"]:
            response = requests.get(place_url)
            response.raise_for_status()

            place_info = response.json()
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
                self.create_image(place_info, place)
