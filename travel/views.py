from django.shortcuts import render, redirect
from user.models import Op_request



def home(request):
    if request.session.has_key('is_logged'):
        return redirect('/user/sign_in/index')
    # elif request.session.has_key('op_is_logged'):
    #     return redirect('/operator/sign_in/index')
    else:
        return render(request,'travel/home.html')

def join_us(request):
    return render(request,'travel/join_us.html')

def contact(request):
    return render(request, 'travel/contact.html')



def sign_in(request):
    return render(request, 'travel/sign_in.html')

def sign_up(request):
    return render(request, 'travel/sign_up.html')

def join_us_submit(request):
    if request.method == 'POST':
       name=request.POST['agency_name']
       mail=request.POST['agency_email']
       message=request.POST['message']
       contact_no=request.POST['contact']
       q=Op_request(agency_name=name,agency_email=mail,message=message,contact_no=contact_no)

       q.save()
       return redirect('/')
    else:
        return render(request, 'travel/join_us.html')


