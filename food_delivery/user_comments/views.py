from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm
from django.shortcuts import get_object_or_404


def project(request):
    post = get_object_or_404(Post)
    # us_comment = Comment.objects.all()
    posts = Post.objects.all()
    comments = post.comments.filter(active=True)  # Список активных комментариев к этой записи
    new_comment = None
    if request.method == 'POST':  # Комментарий был опубликован
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():  # Создайте объект Comment, но пока не сохраняйте в базу данных
            new_comment = comment_form.save(commit=False)  # Назначить текущий пост комментарию
            new_comment.post = post  # Сохранить комментарий в базе данных
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,
                  'user_comments/comments.html',
                  {'post': post,
                   'comments': comments,
                   'new_comment': new_comment,
                   'posts': posts,
                   'comment_form': comment_form})

