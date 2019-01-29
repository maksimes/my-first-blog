from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Profile(models.Model):
    user_gender = (
        ('MAN', 'Мужской'),
        ('WOMAN', 'Женский'))
    gender = models.CharField(choices=user_gender, verbose_name="Пол",
                              max_length=5)
    city = models.CharField(verbose_name="Город", max_length=30, default="")
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile', primary_key=True)
    dateOfBirth = models.DateField(verbose_name="Дата рождения",
                                   default=timezone.now)
    avatar = models.ImageField(blank=True, upload_to="users/",
                               verbose_name='Фотография')

    def __unicode__(self):
        return self.user


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

