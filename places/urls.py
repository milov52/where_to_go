from django.urls import path

from . import views

app_name = "places"

urlpatterns = [
    path("", views.get_index_page, name="index"),
    path("place/<int:place_id>", views.get_api, name="api"),
]
