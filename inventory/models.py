from django.db import models
from django.utils import timezone


class Inventory(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    keyword = models.CharField(max_length=100)
    filename = models.CharField(max_length=200, default=None)
    cost = models.CharField(max_length=5, default='0')
    quantity = models.CharField(max_length=3, default='0')
    text = models.TextField()
    purchased_date = models.DateTimeField(default=timezone.now)
    retired_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
