from django.contrib import admin
from .models import Education, Experience, Contact

# Register your models here.

admin.site.register([Education, Experience, Contact])
