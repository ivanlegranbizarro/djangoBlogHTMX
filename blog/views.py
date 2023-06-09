from django.shortcuts import render

from .models import Post


def home(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {"post": post}
    return render(request, "blog/post_detail.html", context)
