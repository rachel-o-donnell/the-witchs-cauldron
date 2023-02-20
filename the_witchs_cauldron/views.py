from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.models import User
from django.views import generic, View
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.text import slugify
from .models import PostSpell, Categories, Comment, Profile
from .forms import CommentArea, EditComment, SpellForm


class AddSpell(SuccessMessageMixin, View):
    def get(self, request):
        return render(
            request, "add_spell.html", {"spell_form": SpellForm()})

    def post(self, request):
        spell_form = SpellForm(request.POST, request.FILES)

        if spell_form.is_valid():
            spell = spell_form.save(commit=False)
            spell.creator = request.user
            spell.slug = slugify(spell.title)
            spell.save()
            success_url = '/'
            success_message = "Your spell was posted"
            return redirect('home')
        else:
            messages.error(self.request, 'Please fill in all required details')
            spell_form = SpellForm()

        return render(
            request,
            "add_spell.html",
            {
                    "spell_form": spell_form
            },
        )


# class based views allows for re-use - One view can inherit from another
class PostList(generic.ListView):
    model = PostSpell()
    queryset = PostSpell.objects.order_by('-created_on')
    template_name = 'index.html'
    # paginate_by = 6


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
            messages.success(request, "You liked this post")

        return HttpResponseRedirect(reverse('spell_detail', args=[slug]))


class ListCategories(generic.ListView):
    template_name = 'categories.html'
    context_object_name = 'categorylist'

    def get_queryset(self):
        category_content = {
            'category': self.kwargs['category'],
            'related_posts': PostSpell.objects.filter(
                categories__category=self.kwargs['category']).filter(status=1)
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

# Work around for: SuccessMessageMixin not working for DeleteView
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteComment, self).delete(request, *args, **kwargs)


# Profile
# import Profile
# class Profile(View):

#     def profile(request):
#         name = username.name
#         template_name = "profile.html"
#         # success_url = '/'
#         success_message = "Your Profile was created"


class ProfileView(generic.DetailView):
    model = Profile
    template_name = "profile.html"

    def get_context_data(self, *args, **kwargs):
        active_user = Profile.objects.get(id=self.kwargs['pk'])

        context = {
            "active_user": active_user,
        }
        return context

        # 'related_posts': PostSpell.objects.filter(
        #     categories__category=self.kwargs['category']).filter(status=1)
        # return category_content

    # def valid_form(self, form):
    #     user_instance_form = self.request.user
    #     return super().valid_form(form)


# class CreateProfileView(CreateView):
#     model = Profile
#     template_name = "create_profile.html"

#     def valid_form(self, form):
#         user_instance_form = self.request.user
#         return super().valid_form(form)
