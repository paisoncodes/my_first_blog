from django.shortcuts import render
from operator import attrgetter
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger

from articles.models import BlogPost
from articles.views import get_blog_queryset
# Create your views here.


POSTPERPAGE = 10
def homepage_view(request):
    
    context = {}

    query = ""
    if request.GET:
        query = request.GET.get('q', '')
        context['query'] = str(query)
        
    blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)

    # pagination
    page = request.GET.get('page', 1)
    posts_paginator = Paginator(blog_posts, POSTPERPAGE)

    try:
        blog_posts = posts_paginator.page(page)

    except PageNotAnInteger:
        blog_posts = posts_paginator.page(POSTPERPAGE)

    except EmptyPage:
        blog_posts = posts_paginator.page(posts_paginator.num_pages)


    context['blog_posts'] = blog_posts

    return render(request, 'website/home.html', context)

