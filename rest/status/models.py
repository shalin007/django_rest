from django.db import models
from django.contrib.auth import get_user_model
User= get_user_model()
# Create your models here.


def upload_status_image(instance,filename):
   return "status/{user}{filename}".format(user=instance.user,filename=filename)


class StatusQuerySet(models.QuerySet):
    pass

class StatusManager(models.Manager):
    def get_queryset(self):
        return StatusQuerySet(self.model,using=self._db)

class Status(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField(null=True,blank=True)
    image=models.ImageField(upload_to=upload_status_image,null=True,blank=True)
    updated =models.DateTimeField(auto_now=True)
    timestamp=models.DateTimeField(auto_now_add=True)

    objects = StatusManager()

    def __str__(self):
        return str(self.content)[:50]

    @property
    def owner(self):
        return user