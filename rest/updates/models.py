import json
from django.db import models
from django.contrib.auth import get_user_model
from django.core.serializers import serialize
# Create your models here.
User =get_user_model()


def  upload_update_image(instance,filename):
    return "updates/{user}/{filename}".format(user=instance.user,filename=filename)


class UpdateQueryset(models.QuerySet):
    def serialize(self):
        list_values=(self.values("user","content","id"))
        return json.dumps(list_values)
        
class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQueryset(self.model,using=self._db)
    
class Update(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to=upload_update_image,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.content or ""
    
    def serialize(self):
        try:
            image=self.image.url
        except:
            image=""
        data={
            "id":self.id,
            "user":self.user.username,
            "content":self.content,
            
        }
        data = json.dumps(data)
        return data