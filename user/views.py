from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.


def user_register(request):
    message = ""
    form = UserCreationForm()
    # 取得所有all
    # 取得唯一get
    # 取得篩選filter
    # print(User.objects.filter(username="kevin1"))
    if request.method == "POST":
        print(request.POST)
        form = UserCreationForm(
            request.POST
        )  # 多這一行是用在如果密碼二次不同，至少名字會留下不用再重打一次
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        print(username, password1, password2)
        try:
            if len(password1) < 8:
                message = "密碼長度至少包含8個字元"
            elif password1 != password2:
                message = "兩次密碼不匹配"
            else:
                user = User.objects.filter(username=username)
                if len(user) != 0:
                    message = "帳號已經存在!"
                else:
                    User.objects.create_user(
                        username=username, password=password1
                    ).save()
                    message = "註冊成功!"
        except Exception as e:
            print(e)
            message = "網頁出現錯誤..."
    return render(request, "user/register.html", {"form": form, "message": message})
