from django.contrib import admin
from django.utils.html import format_html

from main.models import Films, Genre, Review


class FilmsAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    list_display = ['name', 'producer', 'rating', 'duration', 'image_tag']
    search_fields = 'name'.split()
    list_filter = 'genre'.split()


admin.site.register(Films, FilmsAdmin)
admin.site.register(Genre)
admin.site.register(Review)
