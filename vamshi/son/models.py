from django.db import models

# Create your models here.
class Visitor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.IntegerField()
    purpose = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)