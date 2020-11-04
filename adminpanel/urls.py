
from django.urls import path,include
from . import views


urlpatterns = [

     path('/',views.home,name='login'),
     path('/signup',views.signup,name='signup'),
     path('/login',views.login,name='login'),
     path('/admin_index',views.admin_index,name='admin_index'),
    # path('find/',views.find,name='find'),
    # path('update',views.update,name='update'),
    # path('delete',views.delete,name='delete'),
     path('logout',views.logout,name='logout'),
     # path('/viewrequest',views.viewrequest,name='viewrequest'),
    # path('deletejob',views.deletejob,name='deletejob'),


]