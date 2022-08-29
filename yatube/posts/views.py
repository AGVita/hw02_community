from django.shortcuts import render, get_object_or_404


from .models import Post, Group

POST_COUNT = 10


def index(request):
    posts = Post.objects.all()[:POST_COUNT]
    template = 'posts/index.html'
    context = {
        'posts': posts
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POST_COUNT]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
