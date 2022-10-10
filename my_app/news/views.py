from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category


# Create your views here.

def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    # news = News.objects.order_by("-created_at")
    context: dict = {
        "news": news,
        "title": "List of News",
        "categories": categories,
    }
    # return render(request, "news/index.html", context)
    return render(request, template_name="news/index.html", context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'categories': categories, 'category': category})
