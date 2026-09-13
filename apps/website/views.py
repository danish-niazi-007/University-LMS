from django.shortcuts import render

def home(request):
    return render(request, "index.html")
def departments(request):
    return render(request, "departments.html")
