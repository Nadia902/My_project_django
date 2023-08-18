from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


# class Message(models.Model):
#     # отправитель
#     sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
#     # получатель
#     recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True,
#                                   related_name='messages')
#     name = models.CharField(max_length=200, blank=True, null=True)
#     email = models.EmailField(max_length=200, blank=True, null=True)
#     subject = models.CharField(max_length=200, blank=True, null=True)
#     body = models.TextField()
#     is_read = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.subject
#
#     class Meta:
#         ordering = ['is_read', '-created']
