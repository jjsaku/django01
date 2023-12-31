from django.db import models
from django.contrib import auth

class Post(models.Model):
    title = models.CharField(max_length=120)
    slug = models.CharField(max_length=120)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title
    
class NewTable(models.Model):
    bigint_f = models.BigIntegerField()
    bool_f = models.BooleanField()
    date_f = models.DateField(auto_now=True)
    char_f = models.CharField(max_length=20, unique=True)
    datetime_f = models.DateField(auto_now_add = True)
    decimal_f = models.DecimalField(max_digits=10, decimal_places=2)
    float_f = models.FloatField(null=True)
    int_f = models.IntegerField(default=2010)
    text_f = models.TextField()

    class Meta:
        ordering = ('-decimal_f',)

    def __str__(self):
        return self.bigint_f

class Product(models.Model):
    SIZES = (
        ('S','Small'),
        ('M','Medium'),
        ('L','Large'),
    )
    sku = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    size = models.CharField(max_length=1, choices=SIZES)
    qty = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Maker(models.Model):
    name = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    

    def __str__(self):
        return self.name
    
class PModel(models.Model):
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    url = models.URLField(default='http://i.imgur.com/Ous4iGB.png')

    def __str__(self):
        return self.name
    
class Product2(models.Model):
    pmodel = models.ForeignKey(PModel, on_delete=models.CASCADE, verbose_name='型號')
    nickname= models.CharField(max_length=15, default='超值二手機', verbose_name='摘要')
    description = models.TextField(default='暫無說明')
    year = models.PositiveIntegerField(default=2016, verbose_name='出場年份')
    price = models.PositiveBigIntegerField(default=0, verbose_name='價格')

    def __str__(self):
        return self.nickname
    
class PPhoto(models.Model):
    product = models.ForeignKey(Product2, on_delete=models.CASCADE)
    description = models.CharField(max_length=20, default='產品照片')
    url = models.URLField(default='http://i.imgur.com/Z230eeq.png')
    url = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.description
    
class Maker_test(models.Model):
    country = models.CharField(max_length=10)
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.country
    
class PModel_test(models.Model):
    maker_test = models.ForeignKey(Maker_test, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    url = models.URLField(default='http://i.imgur.com/Ous4iGB.png')

    def __str__(self):
        return self.name
    
class Maker_test2(models.Model):
    country = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=20)

    def __str__(self):
        return self.description
    
class PModel_test2(models.Model):
    maker = models.ForeignKey(Maker_test2, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    url = models.URLField()

    def __str__(self):
        return self.url
    
class Maker_test3(models.Model):
    country = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=20)

    def __str__(self):
        return self.country
    
class PModel_test3(models.Model):
    maker = models.ForeignKey(Maker_test3, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    url = models.URLField()

    def __str__(self):
        return self.url
    

class Mood(models.Model):
    status = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.status
    
class Post2(models.Model):
    mood = models.ForeignKey('Mood', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10, default='不願意透漏身份的人')
    message = models.TextField(null=False)
    del_pass = models.CharField(max_length=10)
    pub_time = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.message
    
class User(models.Model):
    name = models.CharField(max_length=20, null=False)
    email = models.EmailField()
    password = models.CharField(max_length=20, null=False)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(auth.models.User, on_delete=models.CASCADE)
    height = models.PositiveIntegerField(default=160)
    male = models.BooleanField(default=False)
    website = models.URLField(null=True)

    def __str__(self):
        return self.user.username
    
class Diary(models.Model):
    user = models.ForeignKey(auth.models.User, on_delete=models.CASCADE)
    budget = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    note = models.TextField()
    ddate = models.DateField()

    def __str__(self):
        return f'{self.ddate}({self.user})'
    
class Vote(models.Model):
    name = models.CharField(max_length=20)
    no = models.IntegerField()
    sex = models.BooleanField(default=False)
    byear = models.IntegerField()
    party = models.CharField(max_length=20)
    votes = models.IntegerField()

    def __str__(self) -> str:
        return self.name