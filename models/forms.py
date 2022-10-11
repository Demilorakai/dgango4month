from django import forms
from . import models


class PostForm(forms.ModelForm):

    class Meta:
        model = models.Model
        fields = "__all__"


class AddComment(forms.ModelForm):
    class Meta:
        model = models.ModelComment
        fields = "__all__"

