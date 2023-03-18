from django.shortcuts import render, get_object_or_404,HttpResponseRedirect
from django.urls import reverse

from .models import *
from django.contrib import auth
from .forms import UserLoginForm,UserRegisterForm,ImageProfileForm
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

def profile(request):
    prof = request.user
    if request.method == 'POST':
        form = ImageProfileForm(request.POST,request.FILES)
        if form.is_valid():
            # prof.photo = request.FILES
            # prof.save(comit)
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = ImageProfileForm()
    context = {'title':'Личный профиль','form':form}
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

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

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

def single_post(request,post_id):
    post = Products.objects.filter(pk=post_id)
    context = {'title':'Товар','post':post}
    return render(request,'posts/single_post.html',context=context)

def likes(request,pk):
    post = get_object_or_404(Products,pk=pk)
