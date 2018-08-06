from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.


class UserView(View):

    def get(self,request,*args,**kwargs):
        params = request.GET
        print('接受GET传入的参数：',params)
        return HttpResponse('处理一个GET方法。。。')

    def post(self,request,*args,**kwargs):
        params = request.POST
        print('接受POST传入的参数：',params)
        return HttpResponse('处理一个POST方法。。。')

    def put(self,request,*args,**kwargs):
        params = request.body.decode(encoding='utf-8')
        print('接受PUT传入的参数：',params)
        return HttpResponse('处理一个PUT方法。。。')

    def delete(self,request,*args,**kwargs):
        params = request.body.decode(encoding='utf-8')
        print('接受delete传入的参数：',params)
        return HttpResponse('处理一个delete方法。。。')

    def http_method_not_allowed(self, request, *args, **kwargs):
        print("不允许使用的方法。。。")
        return HttpResponse('不支持此方法：%s'% request.method,status=405)


"""
mo版视图
"""
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'
