from .models import Comment, PostSpell
from django import forms


class CommentArea(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class EditComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class SpellForm(forms.ModelForm):
    class Meta:
        model = PostSpell
        fields = ('title', 'description', 'categories', 'items_needed',
                  'content', 'main_image')


class EditSpell(forms.ModelForm):
    class Meta:
        model = PostSpell
        fields = ('title', 'description', 'categories',
                  'items_needed', 'content', 'main_image')
