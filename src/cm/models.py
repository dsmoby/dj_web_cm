from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=250, unique=True)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    

    def __str__(self):
        return self.title

    def __unicode__(self):
        return 

