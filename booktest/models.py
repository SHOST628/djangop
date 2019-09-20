from django.db import models

# Create your models here.

# library class
class BookInfo(models.Model):
    #  CharField : a string, max_length:max length
    btitle = models.CharField(max_length=20)
    #  publish date: type:date
    bpub_date = models.DateField()

    def __str__(self):
        # return book name
        return self.btitle


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20) # hero name
    hgender = models.BooleanField(default=False) # False:Male  ;  True: Famale
    hcomment = models.CharField(max_length=128)
    #  column name farmat : (ralation_property_name)_id  , ex:  hbook_id
    hbook = models.ForeignKey('BookInfo',models.CASCADE)

    def __str__(self):
        # return book name
        return self.hname
