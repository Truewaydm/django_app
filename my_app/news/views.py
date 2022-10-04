from django.shortcuts import render
from django.http import HttpResponse
from .models import News


# Create your views here.

def index(request):
    news = News.objects.all()
    # news = News.objects.order_by("-created_at")
    context: dict = {"news": news, "title": "List of News"}
    # return render(request, "news/index.html", context)
    return render(request, template_name="news/index.html", context=context)
