from django.contrib import admin
from .models import PostSpell
from django_summernote.admin import SummernoteModelAdmin


@admin.register(PostSpell)  # Decorator: Pythonic way of registering models from models.py to admin panel
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')
