from django.urls import path
from .views import signup, login_coder,logout_coder,index,room
app_name = 'app'

urlpatterns = [
    path('',signup, name='signup'),
    path('login/',login_coder, name='login_coder'),
    path('logout/',logout_coder, name='logout_coder'),
    path('index/',index, name='index'),
    path('<str:room_name>',room, name='room'),
]
