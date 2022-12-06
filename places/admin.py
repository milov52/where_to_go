from django.contrib import admin
from django.utils.html import format_html

from .models import Image, Place


# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):


class ImageInline(admin.TabularInline):
    model = Image
    fields = ('place_image', 'preview_image', 'position')

    readonly_fields = ('preview_image',)

    def preview_image(self, obj):
        return format_html('<img src="{url}" width=200px height=auto />'.format(
            url=obj.place_image.url)
        )


@admin.register(Place)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "description_short")
    search_fields = ("title",)
    inlines = [
        ImageInline,
    ]

# admin.site.register(Place, PostAdmin)
admin.site.register(Image)
