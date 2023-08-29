from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
import os.path

class Category(models.Model):
    DESIGN = 'design'
    LIFESTYLE = 'lifestyle'
    PHOTOGRAPHY = 'photography'
    VACATION = 'vacation'
    WORK = 'work'
    HEALTH = 'health'
    
    CATEGORY_CHOICES = [
        (DESIGN, 'Design'),
        (LIFESTYLE, 'Lifestyle'),
        (PHOTOGRAPHY, 'Photography'),
        (VACATION, 'Vacation'),
        (WORK, 'Work'),
        (HEALTH, 'Health'),
    ]

    name = models.CharField(max_length=50, choices=CATEGORY_CHOICES, unique = True)
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.ManyToManyField(Category, related_name='categories')
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
class StandardPost(Post):
    pass
    
class AudioPost(Post):
    # Add the audio field to your model
    audio_file = models.FileField(upload_to='audio')
    
class VideoPost(Post):
    # Add the video field to your model
    video_file = models.FileField(upload_to='video')
    
class GalleryPost(Post):
    photos = models.ManyToManyField('Photo', related_name='gallery_posts_used_in', blank=True)

class Photo(models.Model):
    image = models.ImageField(upload_to='photos', null=True, blank=True)
    caption = models.CharField(max_length=255, null=True, blank=True)
    gallery_post = models.ForeignKey(GalleryPost, on_delete=models.CASCADE, related_name='gallery_photos', null=True, blank=True)
    def str(self):
        return self.caption or str(self.id)
    

