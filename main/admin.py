from django.contrib import admin

from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo', 'position_at_work')
    list_display_links = ('id', 'name', 'position_at_work')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class HomeWorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'pdffile', 'executor')
    list_display_links = ('id', 'title', 'executor')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(HomeWork)

