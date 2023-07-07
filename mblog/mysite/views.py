from django.shortcuts import render
from django.http import HttpResponse, Http404
import random
from mysite.models import Product

def index(request):
    quotes = ['今日事，今日畢',
              '要怎麼收穫，先那麼栽',
              '知識就是力量',
              '一個人的個性就是他的命運'
              ]
    quote = random.choice(quotes)
    return render(request, 'index.html', locals())

def about(request):
    quotes = ['今日事，今日畢',
              '要怎麼收穫，先那麼栽',
              '知識就是力量',
              '一個人的個性就是他的命運'
              ]
    quote = random.choice(quotes)
    return render(request, 'about.html', locals())

def listing(request):
    products = Product.objects.all()
    return render(request, 'list.html', locals())

def disp_detail(request, sku):
    try:
        p = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404('找不到指定的品項編號')
    return render(request, 'disp.html', locals())
def homepage(request):
    year = 2015
    month = 11
    day = 20
    postid = 1

    html = "<a href='{}'>Show the Post</a>"\
    .format(reverse(''))


    return HttpResponse('Hello World!')

def author(request, author_no = 0):
    html = f"<h2>Here is Author:{author_no}'s about page!</h2><hr>"
    return HttpResponse(html)

def listing01(request, yr, mon, day):
    html = f"<h2>List Date is {yr}/{mon}/{day}</h2><hr>"
    return HttpResponse(html)
def post(request, yr, mon, day, post_num):
    html = f"<h2>{yr}/{mon}/{day}:Post Number:{post_num}</h2><hr>"
    return HttpResponse(html)

def index1(request):
    return render(request, 'index1.html', {'msg':'Hello'})
