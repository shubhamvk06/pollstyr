from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy


from django.contrib.auth.models import User, auth
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
from .models import Post

class BlogListView(ListView):
    model=Post
    template_name= 'home.html'
    context_object_name='all_post_list'
    

class BlogDetailView(DetailView):
    model=Post
    template_name='post_detail.html'


class BlogCreateView(CreateView):
    model=Post
    template_name='post_new.html'
    fields='__all__'


class BlogUpdateView(UpdateView):
    model= Post
    template_name='post_edit.html'
    fields=['title','body']

class BlogDeleteView(DeleteView):
    model=Post
    template_name='post_delete.html'
    success_url=reverse_lazy('blog:home')


# class PagesView(TemplateView):
#    template_name='pages.html'


