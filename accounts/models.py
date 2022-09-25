from django.db import models
from django.utils.text import slugify
# Create your models here.


class NavBar(models.Model):
    title = models.CharField(max_length=50)
    parent = models.ForeignKey("self",on_delete=models.SET_NULL,null=True,blank=True)
    icon = models.CharField(max_length=50)
    slug = models.SlugField(null=True,blank=True)
    child_list_flag = models.BooleanField(default=True)
    order_by = models.CharField(max_length=1)

    def save (self,*args,**Kwargs):
        print(self.slug)
        if self.slug: 
            super(NavBar,self).save(*args,**Kwargs)
        else:    
            self.slug = slugify(self.title)
            super(NavBar,self).save(*args,**Kwargs)

    def __str__(self) -> str:
        return self.title    