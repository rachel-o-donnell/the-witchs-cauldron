from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


# Adds a category label to Spell Posts

class Categories(models.Model):
    category = models.CharField(max_length=50)

    # returns a string representaion of an object
    def __str__(self):
        return self.category


# Post a Spell

class PostSpell(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='spell_posts')
    categories = models.ForeignKey(
        Categories, on_delete=models.CASCADE, default='0')
    updated_on = models.DateTimeField(auto_now=True)
    main_image = CloudinaryField('image', default='placeholder')
    description = models.TextField(blank=True)
    items_needed = models.TextField(blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, related_name='spell_likes', blank=True)

    # orders spell posts by most recently created (minus for decending order)
    class Meta:
        ordering = ['-created_on']

    # returns a string representaion of an object
    def __str__(self):
        return self.title

    # returns the number of likes on a spell post
    def no_of_likes(self):
        return self.likes.count()


# Comments

class Comment(models.Model):
    post = models.ForeignKey(
        PostSpell, on_delete=models.CASCADE, related_name='comments')
    username = models.CharField(max_length=70)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    # orders comments by most recently commented
    class Meta:
        ordering = ['created_on']

    # returns a string representaion of an object
    def __str__(self):
        return f"Comment {self.body} by {self.username}"
