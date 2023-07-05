from django.shortcuts import render
from django.http import HttpResponse, Http404
from mysite.models import Product


def about(request):
    html = '''
    <!DOCTYPE html>
    <html>
    <head><title>About Myself</title></head>
    <body>
    <h2>Min-Huang Ho</h2>
    <hr>
    <p>
    Hi, I am Min-Haung Ho. Nice to meet you!
    </p>
    </body>
    </html>
    '''
    return HttpResponse(html)

def listing(request):
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset='utf-8'>
    <title>中古機列表</title>
    </head>
    <body>
    <h2>以下是目前本店販售中的二手機列表</h2>
    <hr>
    <table width=400 border=1 bgcolor='#ccffcc'>
    {}
    </table>
    </body>
    </html>
    '''

    products = Product.objects.all()
    tags = '<tr><td>品名</td><td>庫存量</td></tr>'
    for p in products:
        tags = tags + '<tr><td>{}</td>'.format(p.name)
        tags = tags + '<td>{}</td>'.format(p.price)
        tags = tags + '<td>{}</td></tr>'.format(p.qty)

    return HttpResponse(html.format(tags))

def disp_detail(request, sku):
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset='utf-8'>
    <title>{}</title>
    </head>
    <body>
    <h2>{}</h2>
    <hr>
    <table width=400 border=1 bgcolor='#ccffcc'>
    {}
    </table>
    <a href='/list'>回列表</a>
    </body>
    </html>
    '''
    try:
        p = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404('找不到指定的品項編號')
    
    tags = '<tr><td>品項編號</td><td>{}</td></tr>'.format(p.sku)
    tags = tags + '<tr><td>品項名稱</td><td>{}</td></tr>'.format(p.name)
    tags = tags + '<tr><td>二手售價</td><td>{}</td></tr>'.format(p.price)
    tags = tags + '<tr><td>庫存數量</td><td>{}</td></tr>'.format(p.qty)
    return HttpResponse(html.format(p.name, p.name, tags))

