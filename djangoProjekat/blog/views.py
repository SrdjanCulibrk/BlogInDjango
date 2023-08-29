from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Category, StandardPost, AudioPost, VideoPost, GalleryPost, Post

# Create your views here.
# def firstView(request):  
#     return render(request, 'HTML/index.html')

def secondView(request):  
    return render(request, 'HTML/category.html')

# def thirdView(request):  
#     return render(request, 'HTML/single-standard.html')

class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'HTML/index.html'

class StandardPostList(generic.ListView):
    queryset = StandardPost.objects.all()
    template_name = 'HTML/index.html'
    
class AudioPostList(generic.ListView):
    queryset = AudioPost.objects.all()
    template_name = 'HTML/index.html'
    
class VideoPostList(generic.ListView):
    queryset = VideoPost.objects.all()
    template_name = 'HTML/index.html'
    
class GalleryPostList(generic.ListView):
    queryset = GalleryPost.objects.all()
    template_name = 'HTML/index.html'


#Pojedinacni postovi
class StandardPostView(generic.DetailView):
    model = StandardPost
    template_name = 'HTML/single-standard.html'  
    
class AudioPostView(generic.DetailView):
    model = AudioPost
    template_name = 'HTML/single-audio.html'
    
class VideoPostView(generic.DetailView):
    model = VideoPost
    template_name = 'HTML/single-video.html'
    
class GalleryPostView(generic.DetailView):
    model = GalleryPost
    template_name = 'HTML/single-gallery.html'
    
class CategoryList(generic.ListView):
    queryset = Category.objects.all()
    template_name = 'HTML/category.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_name = self.request.GET.get('category')
        if category_name:
            posts = Post.objects.filter(category__name=category_name)
            context['category_name'] = category_name
        else:
            posts = Post.objects.all()
            context['category_name'] = 'All Categories'
        context['posts'] = posts
        return context
    
class StylesList(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'HTML/styles.html'

#IZMENJENO    
class AboutList(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'HTML/about.html'
    
class ContactList(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'HTML/contact.html'