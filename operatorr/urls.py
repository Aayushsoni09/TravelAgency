from django.urls import path,include
from . import views


urlpatterns = [

     #path('/',views.home,name='login'),
     path('signup',views.opsignup,name='opsignup'),
     path('login',views.oplogin,name='oplogin'),
     path('index',views.opindex,name='opindex'),
     path('logout',views.oplogout,name='oplogout'),
     path('addbus/',views.addbus,name='addbus'),
    # path('find/',views.find,name='find'),
    # path('update',views.update,name='update'),
    # path('delete',views.delete,name='delete'),
    # path('logout',views.logout,name='logout'),
    # path('deletejob',views.deletejob,name='deletejob'),
]