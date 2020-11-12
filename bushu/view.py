# -*- coding: utf-8 -*-
# @Time    : 2020/11/12 9:54 下午
# @File    : view.py
# @Software: PyCharm
from django.http import HttpResponse
def a(request):
    return HttpResponse("ok")

def b(request):
    path = '/Users/a1/PycharmProjects/xuexi/bushu/bushu/image-20190916151807122.png'
    file = open(path, 'rb')

    return HttpResponse(file.read(), content_type='image/png')