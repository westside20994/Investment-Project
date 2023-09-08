from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class CustomUser(AbstractUser):
    # Add custom fields if needed

    # Add a related_name to avoid clashes with the built-in User model
    # groups = models.ManyToManyField(
    #     Group,
    #     verbose_name= ('groups'),
    #     blank=True,
    #     help_text= (
    #         'The groups this user belongs to. A user will get all permissions '
    #         'granted to each of their groups.'
    #     ),
    #     related_name='customuser_set',  # Add this related_name
    #     related_query_name='user',
    # )
    # user_permissions = models.ManyToManyField(
    #     Permission,
    #     verbose_name=('user permissions'),
    #     blank=True,
    #     help_text= ('Specific permissions for this user.'),
    #     related_name='customuser_set',  # Add this related_name
    #     related_query_name='user',
    # )
    pass
