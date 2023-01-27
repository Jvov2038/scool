from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('id',  'school_class',  'school', 'username', 'last_name', 'first_name', 'patronymic', 'get_image', 'email', 'phone_number', 'address')
    search_fields = ('id', 'username', 'last_name', 'first_name', 'patronymic', 'school_class', 'school', 'get_image', 'email', 'phone_number', 'address')
    list_editable = ('email',)
    list_filter = ('username', 'email', 'address', 'school_class',  'school')

    def get_image(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")

    get_image.short_description = 'Фото'


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('school',)
    search_fields = ('school',)
    list_filter = ('school',)


class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ('school_class',)
    search_fields = ('school_class',)
    list_filter = ('school_class',)


admin.site.register(User, UserAdmin)
admin.site.register(SchoolClass, SchoolClassAdmin)
admin.site.register(School, SchoolAdmin)

