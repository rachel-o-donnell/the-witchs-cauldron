from django.contrib import admin
from .models import PostSpell
from django_summernote.admin import SummernoteModelAdmin


# Summernote features for admin panel
@admin.register(PostSpell)  # Decorator: Pythonic way of registering models from models.py to admin panel
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}  # Prepopulates slugfield in admin panel
    summernote_fields = ('content')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
