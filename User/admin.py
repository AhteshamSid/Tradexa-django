from django.contrib import admin

from .models import Post
from .models import User

# admin.site.register()
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'text', 'created_at', 'updated_at']
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email']

