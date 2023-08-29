from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import views
 

from blog.views import PostList
from .views import AboutList, ContactList, StylesList, CategoryList, AudioPostView, GalleryPostView, StandardPostList, AudioPostList, GalleryPostList, StandardPostView, VideoPostList, VideoPostView
urlpatterns = [
    path("blog/", PostList.as_view(), name='blog'),
    
    #Logo
    path('blog/', TemplateView.as_view(template_name='index.html'), name='blog'),
    
    #Stranice
    path("blog/text/", StandardPostList.as_view(), name="text"),
    path("blog/audio/", AudioPostList.as_view(), name="audio"),
    path("blog/video/", VideoPostList.as_view(), name="video"),
    path("blog/gallery/", GalleryPostList.as_view(), name="gallery"),
    
    #Postovi
    path("blog/text/<slug:slug>/", StandardPostView.as_view(), name="single-text"),
    path("blog/audio/<slug:slug>/", AudioPostView.as_view(), name="single-audio"),
    path("blog/video/<slug:slug>/", VideoPostView.as_view(), name="single-video"),
    path("blog/gallery/<slug:slug>/", GalleryPostView.as_view(), name="single-gallery"),

    #Kategorije
    path("category/", CategoryList.as_view(), name='category_list'),
    
    #Styles
    path('styles/', StylesList.as_view(), name='styles'),
    
    #About
    path('about/', AboutList.as_view(), name='about'),
    
    #Contact
    path('contact/', ContactList.as_view(), name='contact'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
