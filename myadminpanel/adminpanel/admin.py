from django.contrib import admin
from .models import *

admin.site.register(MyAdminPanel)
admin.site.register(Author)
admin.site.register(Book)
