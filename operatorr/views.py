from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render,redirect
from user.models import Op_request,Op_info,Vehicle_info
#def home(request):
#    return render(request,'adminpanel/adminlogin.html')

def oplogin(request):
    if request.method == 'POST':

        try:
            username = request.POST['username']
            password = request.POST['password']

            user = Op_info.objects.filter(username=username, password=password)

            if (user.count() == 1):
                request.session['username'] = username
                print(username)
                return redirect('opindex')

            else:

                messages.info(request, 'invalid username or password')
                return redirect("oplogin")

        except:
            return HttpResponse("invalid")
    else:
        return render(request, 'operatorr/login.html')


def opsignup(request):
    if request.method=='POST':
        username = request.POST['username']
        agency_name = request.POST['agency_name']
        contact_person_name = request.POST['contact_person_name']
        contact_person_no = request.POST['contact_person_no']
        email = request.POST['email']
        password = request.POST['password']
        document_no=request.POST['document_no']
        document_name=request.POST['document_name']
        recovery_email=request.POST['recovery_email']
        x = Op_info(username=username,agency_name=agency_name,contact_person_name=contact_person_name,contact_person_no=contact_person_no,email=email,password=password,document_name=document_name,recovery_email=recovery_email,document_no=document_no)
        x.save()
        return redirect('oplogin')
    else:
        return render(request, 'operatorr/signup.html')

def opindex(request):
    #print(Op_info.objects.values_list())
    q = Op_info.objects.filter(username=request.session['username'])
    print(q)
    return render(request,'operatorr/index.html',{'op_data':q})

def oplogout(request):
    del request.session['username']
    return redirect('oplogin')

def viewbus(request):
    j = Vehicle_info.objects.all()
    return render(request, 'operatorr/viewbus.html', {'jobs': j})

def addbus(request):
    if request.method=='POST':
        obj=Vehicle_info(jtitle=request.POST['jtitle'],jcname=request.POST['jcompany'],jobtype=request.POST['job-type'],jstate=request.POST['jstate'],jdistrict=request.POST['jdistrict'],jdesc=request.POST['jdesc'])
        obj.save()
        return redirect('opindex')
    return render(request,'operatorr/addbus.html')

# def viewrequest(request):
#     request_list = Op_request.objects.filter(status=None)
#     request_list_dic = {'request_list': request_list}
#     return render(request,'adminpanel/view_requests.html',request_list_dic)
# def acceptreq(request):
#     request_list = Op_request.objects.filter(status=True)
#     request_list_dic = {'request_list': request_list}
#     return render(request, 'adminpanel/index.html', request_list_dic)
#
#
# def reject_req(request):
#     request_list = Op_request.objects.filter(status=False)
#     request_list_dic = {'request_list': request_list}
#     return render(request, 'adminpanel/index.html', request_list_dic)
#
