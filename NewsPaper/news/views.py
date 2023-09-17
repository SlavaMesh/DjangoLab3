# from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Post
from django.db import models

class NewsList(ListView):
    model = Post
    ordering = '-date'
    template_name = '../templates/flatpages/news.html'
    context_object_name = 'news'


class PostDetail(DetailView):
    model = Post
    # queryset = Post.objects.all().values('text', 'date')
    template_name = '../templates/flatpages/post.html'
    context_object_name = 'post'


