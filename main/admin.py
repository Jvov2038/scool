from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_photo', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}

    def get_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_photo.short_description = 'Фото'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class LectureAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}


class CategoryLectureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class ProgAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo', 'pdffile', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_editable = ('is_published',)
    filter_horizontal = ('registration',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}

    def get_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_photo.short_description = 'Фото'


class CategoryProgAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class HomeWorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'pdffile', 'executor')
    list_display_links = ('id', 'title', 'executor')
    search_fields = ('title',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(CategoryLecture, CategoryLectureAdmin)
admin.site.register(Prog, ProgAdmin)
admin.site.register(CategoryProg, CategoryProgAdmin)
admin.site.register(HomeWork, HomeWorkAdmin)

admin.site.site_title = 'Администрирование сайта'
admin.site.site_header = 'Администрирование сайта'
