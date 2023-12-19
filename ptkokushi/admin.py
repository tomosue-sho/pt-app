from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import birthday

class CommentAdmin(admin.ModelAdmin):
    list_display = ('__int__', 'user','email', 'password1')

admin.site.register(birthday)