from datetime import datetime, timedelta
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.utils import timezone
from celery import shared_task
from .models import Post
from django.conf import settings


@shared_task
def my_task():
    one_week_ago = timezone.now() - timedelta(weeks=1)

# Получаем все посты, опубликованные в течение последней недели
    posts = Post.objects.filter(dateCreation__gte=one_week_ago)

# Получаем список всех пользователей
    users = User.objects.all()

# Отправляем каждому пользователю электронное письмо с последними постами
    for user in users:
        subject = 'Новсти'
        message = 'Новости за последнюю неделю:\n\n'

    # Добавляем каждый пост в текст сообщения
        for post in posts:
            message += f'- {post.tittle}\n'
            message += f'-{post.text}\n'

    # Отправляем письмо пользователю
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])