from django.db import models


class Post(models.Model):  # создаем модель для отзывов
    title = models.CharField(max_length=250)
    body = models.TextField()

    def __str__(self):
        return self.title

# создаем модель непосредственно для текста комментариев


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')  # создаем связь комментариев с моделью для отзывов
    name = models.CharField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)  # сортируем комментарии по дате создания

    def __str__(self):
        return self.name
