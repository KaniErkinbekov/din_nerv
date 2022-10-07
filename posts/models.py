from distutils.command import upload
from turtle import title
from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class ProductManager(models.Manager):
    def add_count(self, user, post):
        obj, created= self.model.object.get_or_create(
        user = user,
        post = post,
        )
        obj.count = obj.count_likes.count()
        obj.save
        return obj

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'post_pics')
    likes = models.ManyToManyField(User, related_name='blog_posts')
    comment = models.ManyToManyField(User, related_name = 'comment')

    
    def total_likes(self):
        return self.likes.count()

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

    def __str__(self):
        return self.title

    
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})


