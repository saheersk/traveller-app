from django.contrib import admin

from places.models import Category, Gallery, Place


class GalleryAdmin(admin.TabularInline):
    list_display = ['place', 'image']
    model = Gallery


class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'place', 'category']

    inlines = [GalleryAdmin]

admin.site.register(Place, PlaceAdmin)


admin.site.register(Category)





