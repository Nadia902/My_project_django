from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def project(request):
    post = get_object_or_404(Post)
    posts = Post.objects.all()
    comments = Comment.objects.filter(active=True)  # Список активных комментариев к этой записи
    paginator = Paginator(comments, 3)  # 3 поста на каждой странице
    page = request.GET.get('page')
    new_comment = None
    if request.method == 'POST':  # Комментарий был опубликован
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)  # Создаем объект Comment, но пока не сохраняем в базу данных
            new_comment.post = post  # Назначить текущий пост комментарию
            new_comment.save()  # Сохранить комментарий в базе данных
    else:
        comment_form = CommentForm()
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, поставим первую страницу
        pages = paginator.page(1)
    except EmptyPage:
        # Если страница больше максимальной, доставить последнюю страницу результатов
        pages = paginator.page(paginator.num_pages)
    return render(request, 'user_comments/comments.html',
                  {'post': post,
                   'page': page,
                   'comments': comments,
                   'new_comment': new_comment,
                   'posts': posts,
                   'pages': pages,
                   'comment_form': comment_form})