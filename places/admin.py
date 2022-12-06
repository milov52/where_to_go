from django.contrib import admin

from .models import Place, Image


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "description_short")
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}
    empty_value_display = "-пусто-"


admin.site.register(Place)
admin.site.register(Image)
