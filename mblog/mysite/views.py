from django.shortcuts import render
from django.http import HttpResponse, Http404
import random
from mysite.models import Product,Product2
from datetime import datetime
from mysite import models

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
    #.format(reverse(''))


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

def index2(request):
    now = datetime.now()
    return render(request, 'index2.html', locals())

def index3(request, tvno = 0):
    tv_list = [
        {'name':'三立', 'tvcode':'oZdzzvxTfUY'},
        {'name':'中視', 'tvcode':'TCnaIE_SAtM'},
        {'name':'中天', 'tvcode':'zMoMuvPCoo4'},
        {'name':'民視', 'tvcode':'ylYJSBUgaMA'},
    ]
    now = datetime.now()
    tv = tv_list[tvno]
    return render(request, 'index3.html', locals())

def index4(request, tvno = 0):
    tv_list = [
        {'name':'三立', 'tvcode':'oZdzzvxTfUY'},
        {'name':'中視', 'tvcode':'TCnaIE_SAtM'},
        {'name':'中天', 'tvcode':'zMoMuvPCoo4'},
        {'name':'民視', 'tvcode':'ylYJSBUgaMA'},
    ]
    now = datetime.now()
    tv = tv_list[tvno]
    hour = now.timetuple().tm_hour
    return render(request, 'index4.html', locals())

def engtv(request, tvno='0'):
    tv_list = [
        {'name':'SkyNews', 'tvcode':'9Auq9mYxFEE'},
        {'name':'Euro News', 'tvcode':'pykpO5kQJ98'},
        {'name':'India News', 'tvcode':'Xmm3Kr5P1Uw'},
        {'name':'CNA News', 'tvcode':'XWq5kBlakcQ'},
    ]
    now = datetime.now()
    tvno = tvno
    tv = tv_list[int(tvno)]
    return render(request, 'engtv.html', locals())

def carlist(request, maker=0):
    car_maker = ['SAAB','Ford','Honda','Mazda','Nissan','Toyota']
    car_list = [
        [],
        ['Fiesta','Focus','Modeo','EcoSport','Kuga','Mustang'],
        ['Fit','Odyssey','CR-V','City','NSX'],
        ['Mazda3','Mazda5','Mazda6','CX-3','CX-5','MX-5'],
        ['Tida','March','Livina','Sentra','Teana','X-Trail','Juke','Murano'],
        ['Camry','Altis','Yaris','86','Prius','Vios','RAV4','Wish']
    ]
    maker = maker
    maker_name = car_maker[maker]
    cars = car_list[maker]
    return render(request, 'carlist.html', locals())

def carprice(request, maker=0):
    car_maker = ['Ford', 'Honda', 'Mazda']
    car_list = [
        [
        {'model':'Fiesta', 'price':203500},
        {'model':'Focus', 'price':605000},
        {'model':'Mustang', 'price':900000}],
        [
        {'model':'Fit', 'price':450000},
        {'model':'City', 'price':150000},
        {'model':'NSX', 'price':1200000}],
        [
        {'model':'Mazda3', 'price':329999},
        {'model':'Mazda5', 'price':603000},
        {'model':'Mazda6', 'price':850000}],
        ]
    maker = maker
    maker_name = car_maker[maker]
    cars = car_list[maker]
    return render(request, 'carprice.html', locals())

def index5(request):
    return render(request, 'index5.html', locals())


def index6(request):
    products = models.Product2.objects.all()
    return render(request, 'index6.html', locals())

def detail(request, id):
    try:
        product = models.Product2.objects.get(id=id)
        images = models.PPhoto.objects.filter(product=product)
    except:
        pass
    return render(request, 'detail.html', locals())
