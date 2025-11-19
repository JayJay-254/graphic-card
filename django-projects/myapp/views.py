from django.shortcuts import render,HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')
def home(request):
    return HttpResponse(request, "hello world")

def about(request):
    return render(request, 'about.html')
def gallery(request):
    return render(request, 'gallery.html')