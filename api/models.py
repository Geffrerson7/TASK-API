from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    priority = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

    def completar(self):
        self.completed_at = timezone.now()
        return self.save()