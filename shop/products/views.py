from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def category_list(request):
    categories = Category.objects.all()
    paginator = Paginator(categories, 6)  # Показывать 6 категорий на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'products/category_list.html', {'page_obj': page_obj, 'categories': page_obj.object_list})

def product_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()
    paginator = Paginator(products, 6)  # Показывать 6 продуктов на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'products/product_list.html', {'category': category, 'page_obj': page_obj, 'products': page_obj.object_list})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})
