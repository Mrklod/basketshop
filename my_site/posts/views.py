from django.shortcuts import render, get_object_or_404,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import auth
from .forms import UserLoginForm,UserRegisterForm,ImageProfileForm,CommentForm
# Create your views here.
def index(request):
    context = {'title':'Главная страница'}
    return render(request,'posts/index.html',context=context)

def contact(request):
    context = {'title':'Контакты'}
    return render(request,'posts/contact.html',context=context)

def about(request):
    context = {'title':'О нас'}
    return render(request,'posts/about.html',context=context)

@login_required
def profile(request):
    prof = request.user
    com = Comment.objects.filter(name=prof).count()
    if request.method == 'POST':
        form = ImageProfileForm(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = ImageProfileForm()
    context = {'title':'Личный профиль',
               'form':form,
               'com':com,
               }
    return render(request,'posts/profile.html',context=context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserRegisterForm()
    context = {'title':'Регистрация','form':form}
    return render(request,'register.html',context=context)

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,password=password)
            if user:
                auth.login(request,user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'title':'Авторизация','form':form}
    return render(request,'login.html',context=context)
@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
@login_required
def catalog(request):
    brend = Brend.objects.all()
    cat = Category.objects.all()
    product = Products.objects.all()
    context = {'title':'Каталог',
               'brend':brend,
               'cat':cat,
               'product':product,
               }
    return render(request,'posts/catalog.html',context=context)
@login_required
def single_post(request,post_id):
    con = Products.objects.filter(id=post_id)
    post = Products.objects.get(id=post_id)
    com = Comment.objects.filter(post=post)
    context = {'title': 'Товар',
               'post': post,
               'comments': com,
               'con':con}
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            posts = form.save(commit=False)
            posts.name = request.user
            posts.post = post
            posts.save()
            context['form'] = posts
            return HttpResponseRedirect(reverse('single_post',args=[post_id]))
    else:
        form = CommentForm
        context['form'] = form
    return render(request,'posts/single_post.html',context=context)

def likes(request,pk):
    post = get_object_or_404(Products,pk=pk)
