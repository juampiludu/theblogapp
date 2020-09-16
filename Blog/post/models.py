from django.db import models
from django.contrib.auth.models import User
from django.contrib.humanize.templatetags.humanize import naturaltime

class Post(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    body_text = models.TextField()
    published_date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return f'{self.title} by {self.author}'

    def formatDate(self):
        return naturaltime(self.published_date)

    def formatTitle(self):
        return self.title.title()

    def add_view(self):
        self.views += 1

class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.post} - {self.author}"

    def formatDate(self):
        return naturaltime(self.published_date)
