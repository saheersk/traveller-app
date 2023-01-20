from django.contrib import admin

from places.models import Category, Gallery, Place, Comment


class GalleryAdmin(admin.TabularInline):
    list_display = ['place', 'image']
    model = Gallery


class PlaceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'place', 'category']

    inlines = [GalleryAdmin]

admin.site.register(Place, PlaceAdmin)


admin.site.register(Category)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'date', 'place', 'comment']

admin.site.register(Comment, CommentAdmin)


# class LikeAdmin(admin.ModelAdmin):
#     list_display = ['id']

# admin.site.register(Like, LikeAdmin)





