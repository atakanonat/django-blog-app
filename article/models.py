from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

# When a model modified:
# python manage.py makemigrations
# python manage.py migrate


class Article(models.Model):
    # on_delete attribute, deletes articles when user account is deleted.
    author = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, verbose_name="Author")
    title = models.CharField(max_length=50, verbose_name="Title")
    content = RichTextField()
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Created Date")
    article_img = models.FileField(blank=True, verbose_name="articleImg")

    # Django Meta options
    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, verbose_name='Article', related_name='comments')
    comment_author = models.CharField(
        max_length=50, verbose_name='commentAuthor')
    comment_content = models.CharField(
        max_length=200, verbose_name='commentContent')
    comment_date = models.DateTimeField(
        auto_now_add=True, verbose_name='commentDate')

    class Meta:
        ordering = ['-comment_date']
