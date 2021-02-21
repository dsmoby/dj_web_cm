from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'text', 'created_on')

admin.site.register(Article, ArticleAdmin)
