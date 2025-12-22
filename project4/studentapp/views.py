from django.shortcuts import render

def home(request):
    return render(request, 'studentapp/home.html')
