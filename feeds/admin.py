from django.contrib import admin
from .models import Post, Roadmap, Career, Solution
# Register your models here.

admin.site.register((Post, Roadmap, Career, Solution))