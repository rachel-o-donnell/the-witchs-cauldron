from django.contrib import admin
from .models import PostSpell, Comment, Categories, Profile
from django_summernote.admin import SummernoteModelAdmin


# Summernote features for admin panel
@admin.register(PostSpell)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content', 'items_needed')
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('created_on',)


# Admin features for comments
@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = (
        'username', 'body', 'post', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('username', 'email', 'body')


# Categories section
admin.site.register(Categories)

admin.site.register(Profile)
