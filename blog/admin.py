from django.contrib import admin
from .models import Post

admin.site.register(Post) 
# luego de registrar el modelo debo realizar las migraciones a la base de datos