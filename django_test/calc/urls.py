from django.urls import path
from . import views 
urlpatterns = [
    path('',views.home, name='home'),
    path('add',views.add,name='add'),
    path('index',views.index,name='index'),
    path('account/signup/',views.account_login,name='account_login'),path('account/signup/new_user',views.new_user,name="new_user")
]
