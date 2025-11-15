from django.shortcuts import render
from .models import Employee

def form_view(request):
    message = ""

    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        Employee.objects.create(name=name, age=age)
        message = "Form submitted successfully!"

    return render(request, "form.html", {"message": message})
