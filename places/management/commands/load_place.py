import os
import urllib.request
from urllib.parse import urlparse

import requests
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.core.management.base import BaseCommand

from places.models import Image, Place


class Command(BaseCommand):
    def handle(self, *args, **options):
        file_name = os.path.dirname(os.path.realpath(__file__)) + "/list"

        with open(file_name) as f:
            places = f.read().splitlines()

        file_prefix = "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/"
        for place in places:
            print(place)
            response = requests.get(file_prefix + place)
            place_info = response.json()
            obj, created = Place.objects.get_or_create(
                title=place_info["title"],
                description_short=place_info["description_short"],
                description_long=place_info["description_long"],
                coord_lng=place_info["coordinates"]["lng"],
                coord_lat=place_info["coordinates"]["lat"],
            )

            images = place_info["imgs"]
            index = 0
            for image_url in images:
                image_name = urlparse(image_url).path.split("/")[-1]

                new_image, created = Image.objects.get_or_create(
                    places=obj,
                    position=index,
                    image=image_name,
                )
                index += 1

                if created:
                    img_temp = NamedTemporaryFile(delete=True)
                    img_temp.write(urllib.request.urlopen(image_url).read())
                    img_temp.flush()
                    new_image.image.save(
                        image_name, File(img_temp), save=True
                    )
