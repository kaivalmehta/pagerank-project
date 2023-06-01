from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"basic_app/home.html")
def about(request):
    return render(request,"basic_app/aboutus.html")
def demo(request):
    return render(request,"basic_app/demo.html")

def zero(request):
    return render(request,"basic_app/page0.html")
def one(request):
    return render(request,"basic_app/page1.html")
def two(request):
    return render(request,"basic_app/page2.html")
def three(request):
    return render(request,"basic_app/page3.html")
def four(request):
    return render(request,"basic_app/page4.html")
