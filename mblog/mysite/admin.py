from django.contrib import admin
from mysite.models import Post
from mysite.models import NewTable
from mysite.models import Product,PModel,PPhoto,Maker,Product2,Maker_test,PModel_test,PModel_test2,Maker_test2,Maker_test3,PModel_test3,Mood,Post2
from mysite import models


admin.site.register(Post)
admin.site.register(NewTable)
admin.site.register(Product)
admin.site.register(Maker)
admin.site.register(PModel)
admin.site.register(PPhoto)
admin.site.register(Maker_test)
admin.site.register(PModel_test)
admin.site.register(Maker_test2)
admin.site.register(PModel_test2)
admin.site.register(Maker_test3)
admin.site.register(PModel_test3)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('pmodel', 'nickname', 'price', 'year')
    search_fields=('nickname',)
    ordering = ('-price',)

admin.site.register(Product2, ProductAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'message', 'enabled', 'pub_time')
    ordering = ('-pub_time',)

admin.site.register(models.Mood)
admin.site.register(models.Post2, PostAdmin)
admin.site.register(models.User)