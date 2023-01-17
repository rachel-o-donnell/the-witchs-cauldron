from .models import Comment
from django import forms


class CommentArea(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
