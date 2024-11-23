from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def detail(request,id):
    return render(request, 'home/info.html')
