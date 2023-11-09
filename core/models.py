from django.db import models
from django.urls import reverse
import uuid
# Create your models here.
class Register(models.Model):
    user_name = models.CharField(max_length=30, verbose_name="First name ")
    user_lastname = models.CharField(max_length=30, verbose_name="Last name ")
    phone_number = models.IntegerField()
    user_email = models.EmailField(max_length=254)
    password = models.CharField(max_length=12)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)


    def __str__(self):
        return self.user_name