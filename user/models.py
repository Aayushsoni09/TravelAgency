from django.db import models
from phone_field import PhoneField

class Op_info(models.Model):
    operator_id = models.AutoField(primary_key=True,
                                  unique=True)
    username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=15)
    agency_name = models.CharField(max_length=100)
    contact_person_name = models.CharField(max_length=30)
    contact_person_no=PhoneField(blank=True)
    email = models.EmailField(unique=True)
    document_name = models.CharField(max_length=20,null=True)
    document_no = models.PositiveIntegerField(null=True)
    recovery_email = models.EmailField(blank=True)

    def __str__(self):
        return self.agency_name

class Op_request(models.Model):
    request_id = models.AutoField(primary_key = True,
                                  unique = True)
    agency_name = models.CharField(max_length=30)
    agency_email = models.EmailField(max_length=250)
    message = models.CharField(max_length=100)
    status = models.BooleanField(null=True)
    contact_no = PhoneField(blank=True)

    def __str__(self):
        return self.request_id

class Vehicle_info(models.Model):
    vehicle_id = models.AutoField(primary_key = True,
                                  unique = True)
    operator = models.ForeignKey(Op_info,on_delete=models.CASCADE)

    no_of_tickets = models.PositiveIntegerField()
    vehicle_name = models.CharField(max_length=30)
    route_starting_point = models.CharField(max_length=30,blank=True)
    route_destination_point = models.CharField(max_length=30,blank=True)

    def __str__(self):
        return self.vehicle_name


class vehicle_time_info(models.Model):
    vehicle = models.OneToOneField(Vehicle_info,
                                   on_delete=models.CASCADE,
                                   primary_key=True)
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    fare = models.PositiveIntegerField()
    driver_phone_no = PhoneField(blank=True)
    def __str__(self):
        return self.vehicle

class Points(models.Model):
    vehicle = models.OneToOneField(Vehicle_info,
                                   on_delete=models.CASCADE,
                                   primary_key=True)
    boarding_point1 = models.CharField(max_length=15,null=False,blank=False)
    boarding_point2 = models.CharField(max_length=15,null=True)
    boarding_point3 = models.CharField(max_length=15,null=True,blank=True)
    boarding_point4 = models.CharField(max_length=15,null=True,blank=True)
    boarding_point5 = models.CharField(max_length=15,null=True,blank=True)

    dropping_point1 = models.CharField(max_length=15,null=False,blank=False)
    dropping_point2 = models.CharField(max_length=15,null=True)
    dropping_point3 = models.CharField(max_length=15,null=True,blank=True)
    dropping_point4 = models.CharField(max_length=15,null=True,blank=True)
    dropping_point5 = models.CharField(max_length=15,null=True,blank=True)

    def __str__(self):
        return self.boarding_point1



class Days(models.Model):
    vehicle = models.OneToOneField(Vehicle_info,on_delete=models.CASCADE,primary_key=True)

    sunday = models.BooleanField(default=False)
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday= models.BooleanField(default=False)


class User_info(models.Model):
    user_id = models.AutoField(primary_key=True,
                                  unique=True)
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=15)
    user_email = models.EmailField()
    user_address = models.CharField(max_length=50,blank=True)
    phone = PhoneField(blank=True)