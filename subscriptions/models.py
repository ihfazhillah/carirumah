from django.db import models

# Create your models here.
class Subscription(models.Model):
    """
    Subscription model:
    """
    email = models.EmailField()
    query = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.email}: {self.query}'

    def __repr__(self):
        return f'{self.email}: {self.query}'


