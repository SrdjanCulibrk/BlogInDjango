from django.contrib import admin
from .models import Category, Photo, Post, StandardPost, AudioPost, VideoPost, GalleryPost
import os
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    
    
admin.site.register(Post, PostAdmin)

#Standard
class StandardPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(StandardPost, StandardPostAdmin)

#audio
class AudioPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on', 'audio_file')
    list_filter = ("status",'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    actions = ['custom_delete_selected']
    
admin.site.register(AudioPost, AudioPostAdmin)

#video
class VideoPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on', 'video_file')
    list_filter = ("status",'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    actions = ['custom_delete_selected']
    
admin.site.register(VideoPost, VideoPostAdmin)

class PhotoInline(admin.TabularInline):
    model = Photo

#gallery
class GalleryPostAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

    def photo_list(self, obj):
        return ", ".join([p.image.url for p in obj.photos.all()])

    list_display = ['title', 'slug', 'author', 'created_on', 'photo_list']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(GalleryPost, GalleryPostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)