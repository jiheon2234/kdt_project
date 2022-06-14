from operator import index
from django.contrib import admin
from django.urls import path,include
from common.views import * 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/',include('board.urls')),
    path('',mainpage,name='mainpage'),
    path('common/',include('common.urls')),
]
