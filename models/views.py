from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms
from .forms import PostForm, AddComment
from django.shortcuts import redirect

from .models import ModelComment


def all_brands(request):
    car = models.Brand.objects.all()
    return render(request, "all_brands.html",{"car":car})


def all_models(request, id):
    shows = get_object_or_404(models.Model, id=id)
    return render(request, "all_models.html", {"shows": shows})


def put_update_shows(request, id):
    show_id = get_object_or_404(models.Model, id=id)
    if request.method == "POST":
        form = forms.PostForm(instance=show_id,
                              data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('Изменения добавлены успешно!')
    else:
        form = forms.PostForm(instance=show_id)
    return render(request, "shows_update.html", {"form":form,
                                                "show":show_id})



def add_comment(request, id):
    method = request.method
    if method == "POST":
        form = forms.AddComment(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Комментарий добавлен успешно!")
    else:
        form = forms.AddComment()
    return render(request, "add_comment.html", {"form":form})
