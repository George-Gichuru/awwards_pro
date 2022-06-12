from django.http  import HttpResponse
from django.shortcuts import render, redirect
from django.http  import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, PostForm,UpdateUserForm,UpdateProfileForm,RateForm
from .models import Post,Profile, User,Rate
from django.db.models import Avg
import math
import random

# Create your views here

def home(request):
    posts = Post.objects.all().order_by("-posted")
    if request.method == 'POST':
        uform = PostForm(request.POST, request.FILES)
        if uform.is_valid():
            post = uform.save(commit=False)
            post.user = request.user
            post.save()
            return HttpResponseRedirect(request.path_info)
    else:
        uform = PostForm()
    return render(request, 'index.html',{'uform': uform,'posts':posts})
    

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'django_registration/registration_form.html', {'form': form})

@login_required(login_url='login')
def profile(request, username):
    return render(request, 'profile.html')


@login_required(login_url='login')
def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return redirect('profile', user.username)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateProfileForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'prof_form': prof_form
    }
    return render(request, 'edit.html', params)

@login_required(login_url='login')
def postdetail(request,post_id):

    post= Post.objects.get(pk=post_id)
    if request.method =='POST':
        form = RateForm(request.POST,request.FILES)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.post= post
            #adding the user here
            rate.user = request.user
            #total calculation
            rate.total = (rate.design+rate.usability+rate.content+rate.creativity)/4
            rate.save()
    else:
        form = RateForm()
    design = Rate.objects.filter(post_id=post_id).aggregate(Avg('design'))['design__avg']
    usability = Rate.objects.filter(post_id=post_id).aggregate(Avg('usability'))['usability__avg']
    content = Rate.objects.filter(post_id=post_id).aggregate(Avg('content'))['content__avg']
    creativity = Rate.objects.filter(post_id=post_id).aggregate(Avg('creativity'))['creativity__avg']
    total = Rate.objects.filter(post_id=post_id).aggregate(Avg('total'))['total__avg']
    
    if design is None:
        design = 0
        content = 0
        usability = 0
        creativity = 0
        total = 0       
        designpercentage = 0
        usabilitypercentage = 0
        contentpercentage = 0
        creativitypercentage = 0
        
    else:
        designpercentage = (design/10) *100
        usabilitypercentage = (usability/10) *100
        contentpercentage = (content/10) *100
        creativitypercentage = (creativity/10) *100

    return render(request,"detail.html", {'design':design,'post':post,'form':form,'usability':usability,'content':content,'total':total,'designpercentage':designpercentage,'usabilitypercentage':usabilitypercentage,'contentpercentage':contentpercentage, 'creativitypercentage':creativitypercentage})

@login_required(login_url='/accounts/login/')
def search_results(request):
    current_user = request.user
    post =Post.objects.filter(user=current_user)
    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_post(search_term)
        message=f"{search_term}"

        return render(request,'search_results.html',{"message":message,"posts":searched_posts,"post":post})

    else:
        message="You haven't searched for any projects"
        return render(request,'search_results.html',{"message":message})
