from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'pages/index.html')


def post(request):
    return render(request,'pages/post.html')

def profile(request):
    return render(request,'pages/profile.html')

def register(request):
    return render(request,'accounts/register.html')

def loginpage(request):
    return render(request,'accounts/login.html')