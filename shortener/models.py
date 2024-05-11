from django.db import models

# Create your models here.
class Url(models.Model):
    link_id = models.CharField(max_length=5)
    link  = models.CharField(max_length=10000)

    def __str__(self):
        return self.link_id
    