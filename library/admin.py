from django.contrib import admin
from .models import Book  # Import your models from the library app

admin.site.register(Book)
# admin.site.register(YourModel2)