from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from .models import *

# Register your models here.

class PictureBlogAdminForm(forms.ModelForm):
    class Meta:
        model=PictureBlog
        fields = '__all__'

class PictureBlogAdmin(admin.ModelAdmin):
    form = PictureBlogAdminForm
    list_display = ('author', 'id', 'created_at', 'photo', 'is_published')
    list_display_links = ('id',)
    search_fields = ('created_at',)
    list_editable = ('is_published',)
    list_filter = ('is_published',)
    fields = ('author', 'photo', 'is_published', 'created_at')
    readonly_fields = ('created_at', 'author')
    # save_on_top = True



admin.site.register(PictureBlog, PictureBlogAdmin)
admin.site.site_title = 'Manage pictures'
admin.site.site_header = 'Manage Pictures'

