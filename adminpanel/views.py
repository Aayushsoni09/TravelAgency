
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib import auth
from user.models import Op_request
def home(request):
    return render(request,'adminpanel/adminlogin.html')

def login(request):
    if request.method=='POST':
        username=request.POST['ausername']
        password=request.POST['apassword']
        x=auth.authenticate(username=username,password=password)
        if x is None:
            return render(request, 'adminpanel/adminlogin.html')

        else:
            request.session['username'] = username
            return render(request,'adminpanel/index.html')
    else:
        return render(request,'adminpanel/adminlogin.html')

def signup(request):
    if request.method=='POST':
        username = request.POST['ausername']
        firstname = request.POST['afirstname']
        lastname = request.POST['alastname']
        email = request.POST['amail']
        password = request.POST['apassword1']
        x = User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
        x.save()
        return redirect('login')
    else:
        return render(request, 'adminpanel/adminsignup.html')

def admin_index(request):
    return render(request,'adminpanel/index.html')

def viewrequest(request):
    request_list = Op_request.objects.filter(status=None)
    request_list_dic = {'request_list': request_list}
    return render(request,'adminpanel/view_requests.html',request_list_dic)

def accepted(request):
    request_list = Op_request.objects.filter(status=True)
    request_list_dic = {'request_list': request_list}
    return render(request, 'adminpanel/index.html', request_list_dic)


def rejected(request):
    request_list = Op_request.objects.filter(status=False)
    request_list_dic = {'request_list': request_list}
    return render(request, 'adminpanel/index.html', request_list_dic)

def logout(request):
    del request.session['uid']
    return redirect('login')
