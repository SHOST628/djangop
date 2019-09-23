from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext
from booktest.models import BookInfo


def my_render(request, template_path, context_dict={}):
    # use module file
    # 1.load module file, module object
    temp = loader.get_template(template_path)
    # 2.define module context: transfer data to module file
    # context = RequestContext(request, {})
    context = context_dict
    # 3.module render: generate standard html content
    res_html = temp.render(context)
    # return to browser
    return HttpResponse(res_html)

# Create your views here.
# 1、define view method
# 2、config url, mapping url and view


# purpose :http://localhost:8000/index
def index(request):
    # return HttpResponse('Welcome...')
    # return my_render(request, 'booktest/index.html')
    return render(request, 'booktest/index.html', {'content':'hello world!', 'list':[i for i in range(1,10)]})


def index2(request):
    return HttpResponse('hello world!')


def show_books(request):
    """show books """
    # 1.search for books data by M
    books = BookInfo.objects.all()
    # 2.use module file
    return render(request, 'booktest/show_books.html', {'books':books})


def detail(request, bid):
    """search for book mapping hero imformation"""
    # 1.according to bid to search for book imformation
    book = BookInfo.objects.get(id = bid)
    # 2. search for hero imformation from book
    heros = book.heroinfo_set.all()
    return render(request, 'booktest/detail.html', {'book':book, 'heros':heros})