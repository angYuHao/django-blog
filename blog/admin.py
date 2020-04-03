from django.contrib import admin

# Register your models here.

from .models import Article, ArticleComments

admin.site.register(Article)
admin.site.register(ArticleComments)
