from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView

from .forms import AddPostForm
from .models import Post


# def home(request):
#     return render(request, 'home.html', {})

class Home(ListView):
    model = Post
    template_name = 'home.html'


class ArticleDetail(DetailView):
    model = Post
    template_name = 'article_details.html'


class AddPost(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            try:
                Post.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления поста')
    else:
        form = AddPostForm()
    return render(request, 'add_page.html')
