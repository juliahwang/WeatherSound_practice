from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass
    email = models.EmailField(null=True, unique=True)


class PlayList1()