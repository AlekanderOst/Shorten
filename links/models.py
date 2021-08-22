from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Links(models.Model):
    long = models.CharField('Long link', max_length=100, unique=False)
    short = models.CharField('Short link', max_length=100, unique=False)
    creator = models.ForeignKey(User, verbose_name='Author ', on_delete = models.CASCADE)

    def get_absolute_url(self):
        return reverse('links')