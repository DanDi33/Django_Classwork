from django.http import HttpResponse
from django.shortcuts import render

posts = [
    {
        "title": "Test post 1",
        "author": "John Dou",
        "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been "
                   "the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of "
                   "type and scrambled it to make a type specimen book.",
        "published_at": "October 1 1992"
    },
    {
        "title": "Test post 12",
        "author": "John Dou",
        "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been "
                   "the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of "
                   "type and scrambled it to make a type specimen book.",
        "published_at": "October 1 1992"
    }
]


# Create your views here.

def home(request):
    context = {
        'posts': posts,
        'title': "Main Blog page"

    }
    return render(request, "blog/home.html", context)


def about(request):
    context = {
        'title': "About"}
    return render(request, "blog/about.html", context)
