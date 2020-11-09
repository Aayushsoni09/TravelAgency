from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from user.models import Op_request, Op_info, Vehicle_info, Days
from django.views.decorators.csrf import csrf_exempt


# def home(request):
#    return render(request,'adminpanel/adminlogin.html')

def oplogin(request):
    if request.method == 'POST':

        try:
            username = request.POST['username']
            password = request.POST['password']

            user = Op_info.objects.filter(username=username, password=password)

            if (user.count() == 1):
                request.session['username'] = username
                return redirect('opindex')

            else:

                messages.info(request, 'invalid username or password')
                return redirect("oplogin")

        except:
            return HttpResponse("invalid")
    else:
        return render(request, 'operatorr/login.html')


def opsignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        agency_name = request.POST['agency_name']
        contact_person_name = request.POST['contact_person_name']
        contact_person_no = request.POST['contact_person_no']
        email = request.POST['email']
        password = request.POST['password']
        document_no = request.POST['document_no']
        document_name = request.POST['document_name']
        recovery_email = request.POST['recovery_email']
        x = Op_info(username=username, agency_name=agency_name, contact_person_name=contact_person_name,
                    contact_person_no=contact_person_no, email=email, password=password, document_name=document_name,
                    recovery_email=recovery_email, document_no=document_no)
        x.save()
        return redirect('oplogin')
    else:
        return render(request, 'operatorr/signup.html')


def opindex(request):
    # print(Op_info.objects.values_list())
    q = Op_info.objects.filter(username=request.session['username'])
    return render(request, 'operatorr/index.html', {'op_data': q})


def oplogout(request):
    del request.session['username']
    return redirect('oplogin')


def viewbus(request):
    j = Vehicle_info.objects.all()
    return render(request, 'operatorr/viewbus.html', {'jobs': j})


@csrf_exempt
def addbus(request):
    if request.method == 'POST':
        bus_no = request.POST['bus_no']
        vehicle_type = request.POST['bustype']
        route_starting_point = request.POST['source']
        route_destination_point = request.POST['destination']
        no_of_seats = request.POST['no_of_seats']
        op_id = None
        for data in Op_info.objects.filter(username=request.session['username']):
            op_id=data.operator_id
        obj = Vehicle_info(operator=Op_info.objects.get(operator_id = op_id),bus_no=bus_no, vehicle_type=vehicle_type,
                           route_starting_point=route_starting_point,
                           route_destination_point=route_destination_point, no_of_seats=no_of_seats)
        obj.save()

        v_id=None
        d=Days()
        days = request.POST.getlist('day[]')
        print(days)
        for data in Vehicle_info.objects.filter(bus_no=bus_no):
            v_id=data.vehicle_id
        d.vehicle = Vehicle_info.objects.get(vehicle_id = v_id)
        for day in days:
            if day.lower() == 'monday':
                d.monday = True
            if day.lower() == 'tuesday':
                d.tuesday = True
            if day.lower() == 'wednesday':
                d.wednesday = True
            if day.lower() == 'thursday':
                d.thursday = True
            if day.lower() == 'friday':
                d.friday = True
            if day.lower() == 'saturday':
                d.saturday = True
            if day.lower() == 'sunday':
                d.sunday = True
        d.save()
        # days.monday=True if request.POST.get('day1')
        return redirect('opindex')
    return render(request, 'operatorr/addbus.html')

