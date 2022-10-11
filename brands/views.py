from django.shortcuts import render, get_object_or_404
from . import models


def all_brands(request):
    car = models.Brand.objects.all()
    return render(request, "all_brands.html",{"car":car})
