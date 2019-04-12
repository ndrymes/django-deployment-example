from django.urls import path
from fourthapp import views
app_name='fourthapp'

urlpatterns =[
    path('user_login/',views.user_login,name='log_in'),
    path('register/',views.register_user,name='register')
]
