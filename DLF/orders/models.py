from django.db import models

# Create your models here.
class Orders(models.Model):
    Item = models.TextField()
    quantity = models.IntegerField(default= 0)
    Accepted = models.BooleanField(default=False)
    Price = models.IntegerField(default = 0)


