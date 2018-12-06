from __future__ import unicode_literals

from djongo import models

# Create your models here.


class Superhero(models.Model):
    #created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    #updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    _id = models.ObjectIdField(default='5c070850beecb360474c552f')
    name = models.CharField(max_length=20, null=True)
    description = models.CharField(max_length=500)
    isFavorite = models.BooleanField(default=True)
    picture = models.BinaryField(null=True)
    
    def __str__(self):
        return self.name

