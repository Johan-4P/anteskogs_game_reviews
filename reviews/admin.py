from django.contrib import admin
from .models import Game, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Game)
class GameAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    fields = ('title', 'slug', 'author', 'featured_image', 'content', 'status', 'excerpt')  

# Register your models here.
admin.site.register(Comment)