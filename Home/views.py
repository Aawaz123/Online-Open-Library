from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Welcome to Homepage")
def Authors(request):
    return render(request, 'Authors.html')

def About(request):
     return render(request, 'About.html')