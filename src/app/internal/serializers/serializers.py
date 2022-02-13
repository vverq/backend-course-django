from rest_framework import serializers
from app.internal.models.telegram_user import TelegramUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = '__all__'
