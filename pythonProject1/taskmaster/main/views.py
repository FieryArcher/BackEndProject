from email.message import EmailMessage

from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, DetailView, CreateView
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.views.generic import ListView
from django.core.mail import send_mail
from .forms import *
from .utils import *

menu = [{'title': "About site", 'url_names': 'about_site'},
        {'title': "New state", 'url_names': 'add_page'},
        {'title': "Contact", 'url_names': 'contact'},
        ]


# class StoryHome(ListView):
#     model = Story
#     template_name = 'main/index.html'
#     extra_context = {'title': 'Main Page DreamCost'}
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['menu'] = menu
#         context['title'] = 'Main Page'
#         context['cat_selected'] = 0
#         return context


class StoryHome(ListView):
    model = Story
    template_name = 'main/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Story.objects.filter(is_published=True)


#
# def index(request):
#     tasks = Task.objects.order_by("-id")
#     cats = Category.objects.all()
#     posts = Story.objects.all()
#
#     context = {
#         'posts': posts,
#         'cats': cats,
#         'menu': menu,
#         'title': 'MAIN PAGE',
#         'cat_selected': 0,
#     }
#
#     return render(request, 'main/index.html', context=context)


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    # if request.method == "POST"
    #     message_name = request.POST['message-name']
    #     message_email = request.POST['message-email']
    #     message = request.POST['message']
    #
    #     send_mail(
    #         message_name,
    #         message,
    #         message_email,
    #         []
    #     )
    return render(request, 'main/contact.html')


def pageNotFound(request, exeption):
    return HttpResponseNotFound('<h1>PAGE NOT FOUND</h1>')


class NewsDetailView(DetailView):
    model = Story
    template_name = 'main/show_post.html'
    context_object_name = 'article'


class ShowPost(DetailView):
    model = Story
    template_name = 'main/post.html'
    # slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context


def delete_post(request, post_id):
    post_to_delete = Story.objects.get(pk=post_id)
    post_to_delete.delete()
    return HttpResponseRedirect('home')


# def show_category(request, cat_id):
#     posts = Story.objects.filter(cat_id=cat_id)
#     cats = Category.objects.all()
#     context = {
#         'posts': posts,
#         'cats': cats,
#         'menu': menu,
#         'title': 'MAIN PAGE',
#         'cat_selected': cat_id,
#     }
#
#     return render(request, 'main/index.html', context=context)


class StoryCategory(ListView):
    model = Story
    template_name = 'main/post.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Story.objects.filter(cat__slug=self.kwargs['cat_id'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        return context


class AddPage(CreateView):
    form_class = PostForm
    template_name = 'main/add_page.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        context['menu'] = menu
        return context


# def addpage(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('home')
#             except:
#                 form.add_error(None, 'Ошибка добавления поста')
#     else:
#         form = PostForm()
#     return render(request, 'main/add_page.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})

def send_message(request):
    email = EmailMessage('Hello', 'Body goes here', '200103481@stu.sdu.edu.kz', ['ndarzhanov3@gmail.com'],
                         headers={'Message-ID': 'foo'},)

    email.attach_file(r'C:\Users\Админ\Pictures\tank.png')
    email.send(fail_silently=False)
    return render(request, 'successfull.html')


def news_home(request):
    posts = Story.objects.all()
    return render(request, 'main/index.html', {'posts': posts})


class NewsUpdateView(UpdateView):
    model = Story
    template_name = 'main/update_post.html'
    fields = ['title', 'content', 'cat']
    success_url = '/news_home/'


class NewsDeleteView(DeleteView):
    model = Story
    template_name = 'main/delete_post.html'
    success_url = '/news_home/'


# class NewsDetailView(DetailView):
#     model = Story
#     template_name = 'main/show_post.html'


def home(request):
    return render(request, 'users/home.html')


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('home')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="main/registration.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"login_form": form})


def logout_user(request):
    logout(request)
    return redirect('login')
