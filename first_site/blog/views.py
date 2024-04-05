from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm


# Create your views here.
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "GET":
        context = {'form': PostForm(instance=post), "id": id}
        return render(request, 'blog/post_form.html', context)
    elif request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'The post is updated')
            return redirect('posts')
        else:
            messages.error(request, "Please check your data")
            return render(request, 'blog/post_form.html', {"form": form})


def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    context = {'post': post}
    if request.method == "GET":
        return render(request, 'blog/post_confirm_delete.html', context)
    elif request.method == "POST":
        post.delete()
        messages.success(request, "The post has been deleted")
        return redirect('posts')


def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        # 'title': "Main Blog page"

    }
    return render(request, "blog/home.html", context)


def create_post(request):
    if request.method == "GET":
        context = {'form': PostForm()}
        return render(request, 'blog/post_form.html', context)
    elif request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Success")
            return redirect('posts')
        else:
            messages.error(request, "Error")
            return render(request, 'blog/post_form.html', {'form': form})
    else:
        return False


def about(request):
    context = {
        'title': "About"}
    return render(request, "blog/about.html", context)
