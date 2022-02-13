from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.internal.models.admin_user import AdminUser
from app.internal.models.telegram_user import TelegramUser


@admin.register(AdminUser)
class AdminUserAdmin(UserAdmin):
    pass


@admin.register(TelegramUser)
class AdminTelegramUser(admin.ModelAdmin):
    list_display = ['id', 'username', ]
    pass
