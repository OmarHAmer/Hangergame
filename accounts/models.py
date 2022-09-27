from django.db import models
from django.utils.text import slugify
# Create your models here.

class ProjectApp(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name  

class NavBar(models.Model):
    app_name = models.ForeignKey(ProjectApp,on_delete=models.SET_NULL,blank=True,null=True)
    title = models.CharField(max_length=50)
    parent = models.ForeignKey("self",on_delete=models.SET_NULL,null=True,blank=True)
    icon = models.CharField(max_length=50)
    slug = models.SlugField(null=True,blank=True)
    child_list_flag = models.BooleanField(default=True)
    order_by = models.CharField(max_length=1)

    def save (self,*args,**Kwargs):

        if self.slug: 
            super(NavBar,self).save(*args,**Kwargs)
        else:    
            self.slug = slugify(self.title)
            super(NavBar,self).save(*args,**Kwargs)

    def __str__(self) -> str:
        return self.title    