from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import PostSpell
from .forms import CommentArea


# class based views allows for re-use - One view can inherit from another
class PostList(generic.ListView):
    model = PostSpell()
    queryset = PostSpell.objects.filter(status=1).order_by('created_on')
    template_name = 'index.html'
    # paginate_by = 6  # can only view this many at a time before adding a page nav-change to 9/continuous?


class SpellDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = PostSpell.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "spell_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_area": CommentArea()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = PostSpell.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_area = CommentArea(data=request.POST)

        if comment_area.is_valid():
            comment_area.instance.email = request.user.email
            comment_area.instance.username = request.user.username
            comment = comment_area.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_area = CommentArea()

        return render(
            request,
            "spell_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_area": CommentArea()
            },
        )
