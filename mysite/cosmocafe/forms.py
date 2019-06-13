from django import forms

from .models import Post, Galery

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "name",
            "email",
            "content",
            "image",
        ]

class GaleryForm(forms.ModelForm):
    class Meta:
        model = Galery
        fields = [
            "image",
        ]