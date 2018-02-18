from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.



    
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