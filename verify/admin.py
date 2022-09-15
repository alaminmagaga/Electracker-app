from django.contrib import admin

from verify.models import NewsArticle


class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('newspaper', 'category', 'news_text', 'label')


# Register your models here.
admin.site.register(NewsArticle, NewsArticleAdmin)