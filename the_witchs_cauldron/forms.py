from .models import Comment, PostSpell
from django import forms
from django_summernote.widgets import SummernoteWidget


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

        widgets = {
            'description': SummernoteWidget(),
            'items_needed': SummernoteWidget(),
            'content': SummernoteWidget(),
            }

    def __init__(self, *args, **kwargs):
        super(SpellForm, self).__init__(*args, **kwargs)
        self.fields['main_image'].label = "Upload your spell image here"

    def __init__(self, *args, **kwargs):
        super(SpellForm, self).__init__(*args, **kwargs)
        self.fields['categories'].help_text = "Hold command while clicking to select multiple categories"


class EditSpell(forms.ModelForm):
    class Meta:
        model = PostSpell
        fields = ('title', 'description', 'categories',
                  'items_needed', 'content', 'main_image')
