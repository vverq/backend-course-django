from django.db import models


class TelegramUser(models.Model):
    id = models.IntegerField(primary_key=True, null=False, blank=False)
    username = models.CharField(max_length=30, null=False, blank=False)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    bio = models.CharField(max_length=150, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    profile_photo = models.ImageField(blank=True)

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return self.username
