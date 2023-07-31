"""
URL configuration for mblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from mysite.views import about,listing,disp_detail, \
index,homepage,author,listing01,post,index1,index2,index3,index4,engtv \
,carlist,carprice,index5,index6,detail,index7,index8, delpost,listing2,posting2 \
,contact,post2db,bmi,index9,login,logout
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("index1/", index1),
    path("index2/", index2),
    path("admin/", admin.site.urls),
    path('about/', about),
    path('list/', listing),
    path('list/<str:sku>/', disp_detail),
    path("", index5),
    path("", index),
    path('homepage/',homepage),
    path('author/<int:author_no>/', author),
    path('listing/<int:yr>/<int:mon>/<int:day>/', listing01),
    path('post/<int:yr>/<int:mon>/<int:day>/<int:post_num>/', post, name='post-url'),
    path('<int:tvno>/', index4, name = 'tv-url'),
    path('engtv/', engtv),
    path('engtv/<int:tvno>/', engtv, name='engtv-url'),
    path('carlist/', carlist),
    path('carlist/<int:maker>/', carlist),
    path('carprice/', carprice),
    path('carprice/<int:maker>/', carprice, name='carprice-url'),
    path('detail/<int:id>', detail, name = 'detail-url'),
    path('index6/', index6),
    path('index7/', index7),
    path('index8/', index8),
    path('delpost/<int:pid>/<str:del_pass>/', delpost),
    path('list2/', listing2),
    path('post2/', posting2),
    path('contact/', contact),
    path('post2db/', post2db),
    path('captcha/', include('captcha.urls')),
    path('bmi/', bmi),
    path('index9/', index9),
    path('login/', login),
    path('logout/', logout),

    #path('<int:tvno>', index3, name = 'tv-url'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
urlpatterns = {
    path('info/', include(my_urlpatterns)),

}
'''