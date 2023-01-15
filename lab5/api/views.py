from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from . import models


def all_products(request):
    products = models.Product.objects.all()
    products_dict = []
    for product in products:
        products_dict.append({
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'amount': product.amount,
            'is_active': product.is_active,
        })
    return JsonResponse(products_dict, safe=False)


def id_product(request, **kwargs):
    product = models.Product.objects.get(id=int(kwargs['id']))
    return JsonResponse({
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'amount': product.amount,
        'is_active': product.is_active,
    }, safe=False)


def all_categories(request):
    categories = models.Category.objects.all()
    categories_arr = []
    for category in categories:
        categories_arr.append({
            'id': category.id,
            'name': category.name,
        })
    return JsonResponse(categories_arr, safe=False)


def id_category(request, **kwargs):
    category = models.Category.objects.get(id=int(kwargs['id']))
    return JsonResponse({
        'id': category.id,
        'name': category.name,
    }, safe=False)


def category_products(request, **kwargs):
    category = models.Category.objects.get(id=int(kwargs['id']))
    return JsonResponse({
        'id': category.id,
        'name': category.name,
    }, safe=False)
