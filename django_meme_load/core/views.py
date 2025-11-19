from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Post

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def like_toggle(request, post_id):
    return HttpResponse(f"Like toggle placeholder for post {post_id}")
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def share_post(request, post_id):
    return HttpResponse(f"Share placeholder for post {post_id}")


# Signup view
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # ✅ UserCreationForm handles username & password
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})


# Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("post_list")
    return render(request, "core/login.html")

# Logout view
def logout_view(request):
    logout(request)
    return redirect("login")

# Post list view
@login_required
def post_list(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "core/post_list.html", {"posts": posts})

# Post detail view
@login_required
def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "core/post_detail.html", {"post": post})

# Profile edit view
@login_required
def profile_edit(request):
    user = request.user
    if request.method == "POST":
        user.username = request.POST.get("username")
        user.email = request.POST.get("email")
        user.save()
    return render(request, "core/profile_edit.html", {"user": user})
