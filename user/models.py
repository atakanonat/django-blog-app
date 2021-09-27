from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_img = models.ImageField(unique=True, upload_to='userImg/',
                                    default="userImg/user-01.png", verbose_name="accountImg")
    userAbout = models.CharField(
        blank=True, max_length=200, verbose_name="userAbout")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.account_img.path)
        img.thumbnail((560, 280))
        img.save(self.account_img.path)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
