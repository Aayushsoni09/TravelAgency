
from django.urls import path,include
from . import views


urlpatterns = [

     path('/',views.home,name='login'),
     path('/signup',views.signup,name='signup'),
     path('/login',views.login,name='login'),
     path('/admin_index',views.admin_index,name='admin_index'),
     path('/acceptreq',views.acceptreq,name='acceptreq'),
     path('/rejectreq',views.rejectreq,name='rejectreq'),
     # path('deletereq',views.deletereq,name='deletereq'),
    # path('update',views.update,name='update'),
    # path('delete',views.delete,name='delete'),
     path('/logout',views.logout,name='logout'),
     path('/viewrequest',views.viewrequest,name='viewrequest'),
    # path('deletereq',views.deletereq,name='deletereq'),


]