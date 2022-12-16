from urllib.parse import urlparse

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Image, Place


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("place_url", nargs="+", type=str)

    def create_place(self, place_info):
       return Place.objects.get_or_create(
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

    def create_image(self, place_info, place):
        images = place_info.get("imgs", [])
        for position, filepath in enumerate(images):
            image_name = urlparse(filepath).path.split("/")[-1]

            content_file = ContentFile(filepath, name=image_name)
            Image.objects.create(
                places=place, image=content_file, position=position
            )

    def handle(self, *args, **options):
        for place_url in options["place_url"]:
            response = requests.get(place_url)
            if response.ok:
                place_info = response.json()
                place, is_place_created = self.create_place(place_info)

                if is_place_created:
                    self.create_image(place_info, place)
