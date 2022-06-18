
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# from app.decorators import unauthenticated_user
from .models import *
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .forms import ProfileForm
from django.db.models import Q
from django.views.generic import TemplateView, ListView



# Create your views here.
def index(request):
    posts=Post.objects.all()
    return render(request,'pages/index.html',{'posts':posts})


def profile(request):
    user=User.objects.all()
    return render(request,'pages/profile.html',{'users':user})



def editProfile(request):
    profiles= Profile.objects.get(user=request.user)
   
    if request.method == 'POST':
       
        prof_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if  prof_form.is_valid():
            
            prof_form.save()
            return redirect('profile')
            
            
    else:
        # user_form = UpdateUserForm(instance=request.user)
        prof_form = ProfileForm(instance=request.user.profile)
             
    context={
        # 'user_form': user_form,
        'prof_form': prof_form,
        'profiles': profiles
          
        }
    return render(request,'pages/editprofile.html',context)


def post(request):
    if request.method=='POST':
        photo=request.FILES.get('photo')
        title=request.POST.get('title')
        description=request.POST.get('description')
        posts=Post(post_img=photo,title=title,description=description,user=request.user)
        posts.save_post()
        print('new post is ',posts)
        return redirect('index')
    return render(request,'pages/addpost.html')

def view_post(request,post_id):
    post = Post.objects.get(id=post_id)
    cxt={
        'post':post
    }
    return render(request,'pages/view_post.html',cxt)


def register(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        email_user=request.POST.get('email_user')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')

        if password1==password2:   
                new_user,create = User.objects.get_or_create(first_name=first_name,last_name=last_name,username=username,email_user=email_user)
                if create:
                    try:
                        validate_password(password1)
                        new_user.password = make_password(password1)
                        new_user.profile.first_name=first_name
                        new_user.profile.last_name=last_name
                        new_user.profile.username=username
                        new_user.profile.email_user=email_user
                        new_user.profile.save()
                        new_user.save()
                        return redirect('login')
                    except ValidationError as e:
                        messages.error(request,'Password error {e} ')
        else:
            messages.error(request,"Passwords do not match")
            return redirect('/register')    

    return render(request,'accounts/register.html')

def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
       
        user=authenticate(username=username,password=password)
        print(user)
        
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request,'User with this credentials not found')

    return render(request,'accounts/login.html')


def logoutUser(request):
    logout(request)
    return redirect('index')

class SearchResultsView(ListView):
    model = Post
    template_name = "pages/search.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("query")
        object_list = Post.objects.filter(
            Q(title__icontains=query)
        )
        return object_list
