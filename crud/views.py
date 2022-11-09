from django.shortcuts import render
from .models import Blog
from .froms import add 
# Create your views here.
def all_post(request):
    post = Blog.objects.all()
    return render(request,'blog/blog.html',{'posts':post})

def single_post(request,id):
    post = Blog.objects.get(id= id)
    return render(request,'blog/single.html',{'posts':post})

def add_post(request):
    if request.method == 'POST':
        form = add(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = add()
    return render(request,'blog/add_post.html',{'form':form})

def edit_post(request,id):
    post = Blog.objects.get(id = id)
    if request.method == 'POST':
        form = add(request.POST, instance=post)
        if form.is_valid():
            form.save()
    else:
        form = add(instance=post)
    return render(request,'blog/add_post.html',{'form':form})
