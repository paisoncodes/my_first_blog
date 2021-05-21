from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.http import HttpResponse

from .models import BlogPost
from .forms import CreateBlogPostForm, UpdateBlogForm
from account.models import Account


def create_blog_view(request):
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    form = CreateBlogPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email=user.email).first()
        obj.author = author
        obj.save()

        form = CreateBlogPostForm()

    context['form'] = form

    return render(request, 'articles/create_blog.html', context)

def detail_blog_view(request, slug):

    context = {}

    blog_post = get_object_or_404(BlogPost, slug=slug)

    context['blog_post'] = blog_post

    return render(request, 'articles/detail_blog.html', context)

def edit_blog_view(request, slug):
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')
    
    blog_post = get_object_or_404(BlogPost, slug=slug)
    if blog_post.author != user:
        return HttpResponse('You are not the author of that post!')
    
    if request.POST:
        form = UpdateBlogForm(request.POST or None, request.FILES or None, instance=blog_post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()

            context['success_message'] = 'Update Successful!'
            blog_post = obj
        form = UpdateBlogForm(
            initial = {
                "title": blog_post.title,
                "body": blog_post.body,
                "image": blog_post.image
            }
        )

        context['form'] = form

        return render(request, 'articles/edit_blog.html', context)

def get_blog_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        posts = BlogPost.objects.filter(
            Q(title__icontains=q) |
            Q(body__icontains=q)
        ).distinct()

        for post in posts:
            queryset.append(post)
    return list(set(queryset))