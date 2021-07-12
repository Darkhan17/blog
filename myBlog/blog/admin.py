from django.contrib import admin

from .models import Author,Project,Blog


# Register your models here.

admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(Project)


