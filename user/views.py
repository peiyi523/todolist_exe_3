from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def user_register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(
            request.POST
        )  # 多這一行是用在如果密碼二次不同，至少名字會留下不用再重打一次
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        print(username, password1, password2)
    return render(request, "user/register.html", {"form": form})
