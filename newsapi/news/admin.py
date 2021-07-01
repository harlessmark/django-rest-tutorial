from django.contrib import admin
from news.models import Journalist, Article

admin.site.register(Journalist)
admin.site.register(Article)