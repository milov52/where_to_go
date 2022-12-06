from django.contrib import admin

from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image

@admin.register(Place)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "description_short")
    search_fields = ("title",)
    inlines = [
        ImageInline,
    ]

# admin.site.register(Place, PostAdmin)
# admin.site.register(Image)
