from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import Image, Place


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    fields = ("image", "preview_image", "position")

    readonly_fields = ("preview_image",)

    def preview_image(self, obj):
        return format_html(
            '<img src="{url}" width=200px height=auto />'.format(
                url=obj.place_image.url
            )
        )


@admin.register(Place)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "description_short")
    search_fields = ("title",)
    inlines = [
        ImageInline,
    ]
