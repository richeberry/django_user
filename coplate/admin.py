from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
admin.site.register(User, UserAdmin)
# admin 페이지에는 닉네임 필드가 없으므로 custom field를 만들어서 닉네임 필드를 만듦
# error
UserAdmin.fieldsets += ("Custom fields", {"fields": ("nickname", "kakao_id", "address",)}),