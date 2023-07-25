from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import random
from mysite.models import Product,Product2,Post2,Mood
from datetime import datetime
from mysite import models, forms
from django.core.mail import EmailMessage

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

def index7(request):
    try:
        urid = request.GET['user_id']
        urpass = request.GET['user_pass']
        byear = request.GET['byear']
        urfcolor = request.GET.getlist('fcolor')

    except:
        urid = None
        
    if urid != None and urpass == '12345':
        verified = True
    else:
        verified = False
    years = range(1960,2024)
    return render(request, 'index7.html', locals())

def index8(request):
    posts = models.Post2.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = models.Mood.objects.all()
    try:
        user_id = request.GET['user_id']
        user_pass = request.GET['user_pass']
        user_post = request.GET['user_post']
        user_mood = request.GET['mood']
    except:
        user_id = None
        message = '如要張貼訊息，則每一個欄位都要填...'

    if user_id != None:
        mood = models.Mood.objects.get(status=user_mood)
        post = models.Post2(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
        post.save()
        message=f'成功儲存!請記得你的編輯密碼[{user_pass}]!，訊息需經審查後才會顯示。'

    return render(request, 'index8.html', locals())

def delpost(request, pid=None, del_pass=None):
    if del_pass and pid:
        try:
            post = models.Post2.objects.get(id=pid)
            if post.del_pass == del_pass:
                post.delete()
        except:
            pass
    return redirect('/index8')

def listing2(request):
    posts = models.Post2.objects.filter(enabled=True).order_by('-pub_time')[:150]
    moods = models.Mood.objects.all()
    return render(request, 'listing2.html', locals())

def posting2(request):
    moods = models.Mood.objects.all()
    message = '如要張貼訊息，則每一個欄位都要填...'
    if request.method=='POST':
        user_id = request.POST.get('user_id')
        user_pass = request.POST.get('user_pass')
        user_post = request.POST.get('user_post')
        user_mood = request.POST.get('mood')

        if user_id != None:
            mood = models.Mood.objects.get(status=user_mood)
            post = models.Post2(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
            post.save()
            return redirect('/list2/')

    return render(request, 'posting2.html', locals())

def contact(request):
    if request.method == 'POST' :
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            message = "感謝您的來信。"
            user_name = form.cleaned_data['user_name']
            user_city = form.cleaned_data['user_city']
            user_school = form.cleaned_data['user_school']
            user_email = form.cleaned_data['user_email']
            user_message = form.cleaned_data['user_message']

            mail_body = f'''
            網友姓名:{user_name}
            居住城市:{user_city}
            是否在學:{user_school}
            電子郵件:{user_email}
            反應意見:如下
            {user_message}
            '''

            email = EmailMessage(
                '來自【不吐不快】網站的網友意見',
                mail_body,
                user_email,
                ['jjsaku123@gmail.com','asdfhypnosis@gmail.com']
            )
            email.send()
        else:
            message = "請檢查您輸入的資訊是否正確!"
    else:
        form = forms.ContactForm()
    return render(request, 'contact.html', locals())

            

