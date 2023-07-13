from django.contrib import admin
from mysite.models import Post
from mysite.models import NewTable
from mysite.models import Product,PModel,PPhoto,Maker,Product2,Maker_test,PModel_test,PModel_test2,Maker_test2,Maker_test3,PModel_test3

admin.site.register(Post)
admin.site.register(NewTable)
admin.site.register(Product)
admin.site.register(Maker)
admin.site.register(PModel)
admin.site.register(Product2)
admin.site.register(PPhoto)
admin.site.register(Maker_test)
admin.site.register(PModel_test)
admin.site.register(Maker_test2)
admin.site.register(PModel_test2)
admin.site.register(Maker_test3)
admin.site.register(PModel_test3)

