from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from .models import Post
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.


def post_detail(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,
                           status='published',
                           publish__year=year,
                           publish__month=month,
                           publish__day=day)
    return render(request,'post_detail.html',
    {'post':post}
    )
    
def index(request):
    posts=Post.objects.all()
    paginator=Paginator(posts,3)
    page=request.GET.get('page')
    try:
        page_posts=paginator.page(page)
    except PageNotAnInteger:
        page_posts=paginator.page(1)
    except EmptyPage:
        page_posts=paginator.page(paginator.num_pages)
    return render(request,'index.html',{'posts':page_posts})

def contact(request):

    return render(request,'contact.html')