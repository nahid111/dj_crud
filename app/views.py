from django.shortcuts import render
from .models import Product, Category


def index(request):
    context = {
        'categories': Category.objects.all(),
        'products': Product.objects.all()
    }
    for c in Product.objects.all():
        print(c.photo)
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


