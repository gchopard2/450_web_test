from django.contrib import admin
from .models import Book
from .models import DVD

# Register my models
admin.site.register(Book)
admin.site.register(DVD)