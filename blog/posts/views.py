from django.shortcuts import get_object_or_404, render, redirect
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.





def detail(request, id):
    post = get_object_or_404(Post, pk = id) #pk is primary key
    return render(request, "posts/detail.html", {"post": post })


def delete(request, id):
    post = get_object_or_404(Post, pk = id)
    post.delete()
    return redirect("/")

@login_required()
def new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = PostForm()  #blank form
    return render(request, "posts/new.html", {"form": form})