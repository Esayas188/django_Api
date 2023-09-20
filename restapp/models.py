from django.db import models

# Create your models here.
class Owner(models.Model):
    name = models.CharField(verbose_name= 'Name',blank=False,null=False,max_length=20)
    def __str__(self):
        return self.name

class Drinks(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL ,null=True)
    name = models.CharField(verbose_name= 'Name',blank=False,null=False,max_length=20)
    description = models.TextField(verbose_name='description',max_length=300 )

    def __str__(self):
        return self.name

