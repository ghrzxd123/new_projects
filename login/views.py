from django.shortcuts import render
from django.views.decorators.http import require_POST
from .models import UserInfo


# Create your views here.


def index(request):
    """登录页面"""
    username = request.session.get('userName')
    if username is not None and username.strip() !='':
        return render(request, 'login_success.html', {'username':username})
    else:
        return render(request, 'login.html')


@require_POST
def login_to(request):
    # 获取参数
    username = request.POST.get('userName')
    password = request.POST.get('password')
    # 判断参数是否为空
    if username is None or username.strip() == '':
        context = {'userNameMessage':'账号不能为空'}
        return render(request, "login.html", context)
    if password is None or password.strip() == '':
        context = {'passwordMessage':'密码不能为空', 'userName':username}
        return render(request, "login.html", context)
    try:
        # print(111)
        user = UserInfo.objects.get(userName=username,password=password)
        # 记住登录状态
        request.session['userName'] = user.userName
        return render(request, "login_success.html", {'userName':username})
    except UserInfo.DoesNotExist as e:
        context = {'Message':'账号或密码错误','username':username,'password':password}
        return render(request, 'login.html', context)


def log_out(request):
    request.session.flush()
    return render(request,'login.html')