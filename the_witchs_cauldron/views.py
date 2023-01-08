from django.shortcuts import render
from django.views import generic
from .models import PostSpell


# class based views allows for re-use - One view can inherit from another
class PostList(generic.ListView):
    model = PostSpell()
    queryset = PostSpell.objects.filter(status=1).order_by('created_on')
    template_name = 'index.html'
    #paginate_by = 6  # can only view this many at a time before adding a page nav-change to 9/continuous?
