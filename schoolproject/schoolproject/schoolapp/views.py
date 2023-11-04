from django.shortcuts import render

# Create your views here.
def demo(request):
    return render(request,"home.html")
def login(request):
    return render(request,"login.html")
def register(request):
    return render(request,"register.html")
