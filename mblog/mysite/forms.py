from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from mysite import models
from captcha.fields import CaptchaField

class ContactForm(forms.Form):
    CITY = [
        ['TP', 'Taipei'],
        ['TY', 'Taoyuang'],
        ['TC', 'Taichung'],
        ['TN', 'Tainan'],
        ['KS', 'Kaohsiung'],
        ['NA', 'Others'],
    ]
    user_name = forms.CharField(label='您的姓名', max_length=50, initial='李大仁')
    user_city = forms.ChoiceField(label='居住城市', choices=CITY)
    user_school = forms.BooleanField(label='是否在學', required=False)
    user_email = forms.EmailField(label='電子郵件')
    user_message = forms.CharField(label='您的意見', widget=forms.Textarea)

class PostForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = models.Post2
        fields = ['mood', 'nickname', 'message', 'del_pass']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['mood'].label = '現在心情'
        self.fields['nickname'].label = '你的暱稱'
        self.fields['message'].label = '心情留言'
        self.fields['del_pass'].label = '設定密碼'
        self.fields['captcha'].label = '確定你不是機器人'

class LoginForm(forms.Form):
    COLORS = [
        ['紅', '紅'],
        ['黃', '黃'],
        ['綠', '綠'],
        ['紫', '紫'],
        ['藍', '藍'],
    ]
    user_name = forms.CharField(label='你的姓名', max_length=10)
    user_color = forms.ChoiceField(label='幸運顏色', choices=COLORS)

class LoginForm2(forms.Form):
    username = forms.CharField(label='姓名', max_length=10)
    password = forms.CharField(label='密碼', widget=forms.PasswordInput())
