from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='fallback.png', blank=True) # reqires Pillow
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

    ### create fdrom shell ###
    # >>> from posts.model import Post
    # >>> from posts.models import Post
    # >>> p = Post()
    # >>> p
    # <Post: Post object (None)>
    # >>> p.title = "Post number 1"
    # >>> p.save()

    ### retrieve from db ###
    # >>> Post.objects.all()