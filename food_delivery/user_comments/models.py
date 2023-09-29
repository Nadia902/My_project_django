from django.db import models
from django.contrib.auth.models import User
from users.models import Profile


class Post(models.Model):  # создаем модель для отзывов
    title = models.CharField(max_length=250)
    body = models.TextField()

    def __str__(self):
        return self.title

# создаем модель непосредственно для текста комментариев


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментариев'
        constraints = [
            models.UniqueConstraint(fields=["post", "author"], name="One comment per user per product")
        ]

    def __str__(self):
        return self.name
