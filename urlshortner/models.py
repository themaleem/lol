from django.db import models
from django.conf import settings
# Create your models here.

import random, string
def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

class Link(models.Model):
  attach  = models.CharField(max_length=100,unique=True)
  niickname = models.CharField(max_length=20)
  url= models.URLField(max_length=200)
  owner=models.ForeignKey(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='links')

  def save(self,*args,**kwargs):
    self.attach = randomword(10)
    super(Link,self).save(*args,**kwargs)

  def __str__(self):
    return self.niickname +' '+ self.attach