from django.urls import path

from . import views

app_name='board'
urlpatterns = [
    path('', views.index,name='index'),
    path('<int:mainpost_id>',views.detail,name='detail'),
    path('mainpost_create',views.mainpost_create,name='create')
]