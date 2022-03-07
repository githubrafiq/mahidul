from django.contrib import admin
from .models import Education, Experience, Details

# Register your models here.

admin.site.register([Education, Experience, Details])
