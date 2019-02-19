from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField("Заголовок",  max_length=200)
    text = models.TextField("Текст поcта")
    created_date = models.DateTimeField("Дата создания",
            default=timezone.now)
    published_date = models.DateTimeField("Дата публикации",
            blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='likes', default=0,
                                   blank=True, null=True)

    @property
    def total_likes(self):
        return self.likes.count()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comments(models.Model):
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField("Ответ")
    comments_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    published_date = models.DateTimeField("Дата публикации",
        default=timezone.now)

    def publish(self):
        self.send_date = timezone.now()
        self.save()

class Feedback(models.Model):
    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"

    author = models.ForeignKey("auth.User", on_delete=models.CASCADE,
                               blank=True, null=True)
    name = models.CharField("Имя", max_length=30, blank=True, null=True)
    email = models.EmailField("E-mail", max_length=30)
    text = models.TextField("Текст сообщения")
    send_date = models.DateTimeField("Дата отправки",
                                     default=timezone.now)