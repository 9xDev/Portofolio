from django.shortcuts import render

def home(request):
    return render(request, 'app/index.html',)

def blog(request):
    return render(request, 'app/blog_original.html',)
