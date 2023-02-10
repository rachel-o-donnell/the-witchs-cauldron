from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# from django.urls import reverse_lazy
from .models import PostSpell, Categories, Comment
from .forms import CommentArea, EditComment

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
        comments = post.comments.order_by('created_on')
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
        comments = post.comments.order_by('created_on')
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
            messages.success(request, "Your comment has been posted")
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


class SpellLike(View):

    def post(self, request, slug):
        # gets relevant post
        post = get_object_or_404(PostSpell, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('spell_detail', args=[slug]))


class ListCategories(generic.ListView):
    template_name = 'categories.html'
    context_object_name = 'categorylist'

    def get_queryset(self):
        category_content = {
            'category': self.kwargs['category'],
            'related_posts': PostSpell.objects.filter(categories__category=self.kwargs['category']).filter(status=1)
        }
        return category_content


def category_list(request):
    category_list = Categories.objects.all()
    context = {
        "category_list": category_list,
    }
    return context


# Edit a comment
class EditComment(SuccessMessageMixin, generic.UpdateView):
    model = Comment
    template_name = "edit_comment.html"
    form_class = CommentArea
    success_url = '/'
    success_message = "Your comment was updated"


# Delete a comment
class DeleteComment(SuccessMessageMixin, generic.DeleteView):
    model = Comment
    template_name = "delete_comment.html"
    form_class = CommentArea
    success_url = '/'
    success_message = "Your comment was deleted"
