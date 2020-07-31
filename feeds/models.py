from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.db.models.signals import pre_save
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=300, null=True, blank=True, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})
        

def create_slug(instance, new_slug = None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s"%(slug,qs.first().pk)
        return create_slug(instance,new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver,Post)


class Roadmap(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Career(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Solution(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='solutions')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    solution = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return '%s - %s' %(self.post.title, self.author)

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.post.slug)])
