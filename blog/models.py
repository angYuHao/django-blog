from django.db import models
from datetime import datetime

# Create your models here.
class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.TextField()
    brief_content = models.TextField()
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ArticleComments(models.Model):
    """评论"""
    article = models.IntegerField(verbose_name="文章id")
    comments = models.CharField(max_length=200, verbose_name=u"评论")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"评论"
        verbose_name_plural = verbose_name
