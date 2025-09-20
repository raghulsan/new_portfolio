# views.py
from django.shortcuts import render, redirect
from .models import Contact

def index(request):
    posts = [
        {"id": 1, "title": "Front-end"},
        {"id": 2, "title": "Back-end"},
        {"id": 3, "title": "Animation"},
    ]
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        Contact.objects.create(name=name, email=email, message=message)
        return redirect("portfolio_app:index")  # refresh after save

    return render(request, "app/index.html", {"posts": posts})

def detail(request, post_id):
    return render(request, 'app/detail.html', {"post_id": post_id})

