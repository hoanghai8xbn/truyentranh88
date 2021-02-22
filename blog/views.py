from django.shortcuts import render, HttpResponse
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
import math

p = Post.objects.all()
p2 = []

for i in range(10):
    p2.append(p[i])

max = math.trunc(Post.objects.count() / 10)
if Post.objects.count() / 10 != 0:
    max = max + 1


class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['n'] = p2
        context['arr'] = [1,2,3,4,5]
        context['max'] = max
        return context

def viewlist(request, pk):
    number = pk
    if number <= 3:
        number = 3
    if number + 2 > max and number - 5 >= 0:
        number = max - 2
    lp = []
    arrs = []
    for i in range(number-2,number+3):
        if i <= max:
            arrs.append(i)
    for i in range((pk-1)*10,pk *10):
        if i < Post.objects.count():
            lp.append(p[i])
    return render(request, 'blog/home.html', {"lp":lp, "arrs":arrs})

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/detail.html"

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ["title", "content"]
    template_name = "blog/new.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name = "blog/update.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
        model = Post
        success_url = 'http://127.0.0.1:8000/blog/'
        template_name = "blog/delete.html"

        def test_func(self):
            post = self.get_object()
            if self.request.user == post.author:
                return True
            return False

def detail2(request):
    n = [i for i in range(1, 1+5)]
    return render(request, 'blog/detail2.html', {"n":n})

def detail3(request, pk):
    p = Post.objects.get(pk=pk)
    if pk <= 3:
        pk = 3
    if pk + 1 >= Post.objects.count():
        pk = Post.objects.count() - 2
    arr = [i for i in range(pk - 2, pk + 3)]
    return render(request, 'blog/detail2.html', {"p":p, "arr":arr})