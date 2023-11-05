from django.contrib import admin
from .models import Category, Heroes, Gender

admin.site.register(Heroes)
admin.site.register(Category)
admin.site.register(Gender)
