from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def registration(request):
    return render(request,'registration.html')

def login(request):
    return render(request,'login.html')

# def extra(request):
#     return render(request,'extra.html')  