from django.contrib import admin
from booktest.models import BookInfo,HeroInfo


# user defined
class BookInfoAdmin(admin.ModelAdmin):
    """book model managing class"""
    list_display = ['id', 'btitle', 'bpub_date']


class HeroInfoAdmin(admin.ModelAdmin):
    """hero model managing class"""
    list_display = ['id', 'hname', 'hcomment']


# Register your models here.
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)