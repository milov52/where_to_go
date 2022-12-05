from django.contrib import admin

from .models import Place


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "description_short")
    search_fields = ("title",)
    empty_value_display = "-пусто-"


admin.site.register(Place)
