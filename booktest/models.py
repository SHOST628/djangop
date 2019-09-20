from django.db import models

# Create your models here.

# library class
class BookInfo(models.Model):
    #  CharField : a string, max_length:max length
    btitle = models.CharField(max_length=20)
    #  publish date: type:date
    bpub_date = models.DateField()