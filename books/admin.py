from django.contrib import admin
from .models import Place, Publisher, Title, Category, Book


admin.site.register(Place)
admin.site.register(Publisher)
admin.site.register(Title)
admin.site.register(Category)
admin.site.register(Book)

