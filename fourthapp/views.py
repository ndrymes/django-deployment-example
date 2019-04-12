from django.shortcuts import render
from fourthapp.forms import ProfileInfoForm,UserInfo


from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'fourthapp/index.html')

def register_user(request):

    registered=False


    if request.method=='POST':
        user_info=UserInfo(data=request.POST)
        profile_info=ProfileInfoForm(data=request.POST)


        if user_info.is_valid() and profile_info.is_valid():
            user=user_info.save()
            user.set_password(user.password)
            user.save()

            profile=profile_info.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

                profile.save()
                registered=True

        else:
            print(user_info.errors,profile_info.errors)

    else:
        user_info=UserInfo()
        profile_info=ProfileInfoForm()

    return render(request,'fourthapp/register.html',{'profile_info':profile_info,
                                                     'user_info':user_info,
                                                     'registered':registered})


def user_login(request):

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username='username',password='password')

        if user:
            if user.is_active:
                login(request,user)

                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('your account is not active')
        else:
            print('someone tried to log in')
            print('the username is: {} and password is: {}'.format(username,password))
            return HttpResponse('insert the correct details')

    else:
        return render(request,'fourthapp/log_in.html',{})

@login_required
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
@login_required
def special(request):
    return render(request,'fourthapp/special.html')
