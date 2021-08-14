from django.shortcuts import render

from User.models import Post
from .models import Products


def products(request):
    products = Products.objects.all()
    posts = Post.objects.all()
    return render(request, 'home.html',
                  {'products': products,
                   'posts': posts
                   })
