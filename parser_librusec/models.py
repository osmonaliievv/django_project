from django.db import models


class LibrusecParser(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    img = models.ImageField(upload_to='images/', null=False, default='default.jpg')


    def __str__(self):
        return self.title
