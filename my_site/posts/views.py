from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'posts/index.html')

def contact(request):
    return render(request,'posts/contact.html')

def about(request):
    return render(request,'posts/about.html')

def profile(request):
    return render(request,'posts/profile.html')