from django.shortcuts import render, redirect
from user.models import Op_request
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def home(request):
    if request.method == 'POST':

        return  redirect('indexsubmit')
    return render(request,'travel/index.html')

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

@csrf_exempt
def indexsubmit(request):
    if request.method == 'POST':
        pass
    source = request.POST.get('frome', False);
    # destination = request.POST.get('to')
    # type = request.POST.get('type')
    # person = request.POST.get('person')
    # date = request.POST.get('date')
    print(source)
    return render(request,'travel/index.html')

