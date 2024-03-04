from django.db import models
from django.contrib.auth.models import User


# Create your models here.


# class CustomUser(AbstractUser):
#     teacher_status = models.BooleanField(default=False)
#
#     class Meta:
#         verbose_name = "Custom User"
#         verbose_name_plural = "Custom Users"
#
#     groups = models.ManyToManyField(
#         Group,
#         verbose_name="groups",
#         blank=True,
#         help_text="The groups this user belongs to. A user will get all"
#                   " permissions granted to each of their groups",
#         related_name="customuser_groups"
#     )
    # class Meta:
    #     swappable = "AUTH_USER_MODEL"

class Status(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    teacher_status = models.BooleanField(default=False)





