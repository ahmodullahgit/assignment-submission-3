from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def home_view(request):
    blog = Blog.objects.all().first()
    featured_post = Post.objects.filter(featured=True)[:4]
    story_post = Post.objects.filter(featured=False)
    category = Categories.objects.all()
    context = {'blog': blog, 'featured_post': featured_post, 'story_post': story_post, 'category': category}
    return render(request, 'blog/index.html', context)

def single_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    category = Categories.objects.all()
    posts = Post.objects.all()[::-1][0:10]
    context = {'post': post, "posts":posts, 'category': category}
    return render(request, 'blog/post.html', context)

def categories(request,slug):
    categori = Categories.objects.get(slug=slug)
    category_list = Categories.objects.all() 
    context={'categori':categori,'category': category_list}
    return render(request,'blog/categories.html',context)