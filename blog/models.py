from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField("Заголовок",  max_length=200)
    text = models.TextField("Текст поcта")
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comments(models.Model):
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField("Ответ")
    comments_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    published_date = models.DateTimeField(
        default=timezone.now)

    def publish(self):
        self.send_date = timezone.now()
        self.save()