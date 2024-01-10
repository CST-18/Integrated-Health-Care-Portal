# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from service.models import Contact, Patient ,UserProfile, Doctor
from django.core.exceptions import ObjectDoesNotExist
from service.models import UserProfile, Apps

@login_required
def Home(request):
    return render(request, 'Home.html', {})

def Register(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        phno = request.POST.get('number')
        password = request.POST.get('password')

        new_user = User.objects.create_user(name, email, password)
        new_user.phno = phno

        new_user.save()
        return redirect('loginpage')
    return render(request,'Register.html', {})

def Login(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return HttpResponse('Error, user does not exist')
    return render(request,'Login.html', {})

def logoutuser(request):
    logout(request)
    return redirect('loginpage')

def Aboutus(request):
    return render(request,'Aboutus.html', {})
    
def Services(request):
    return render(request,'Services.html', {})

def Contactus(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        messages = request.POST['add']
        ins = Contact(username=username,add=messages, email=email)
        ins.save()
        print("ok")
    return render(request,'Contactus.html', {})

def Patientdetails(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        gender = request.POST['gender']
        date_of_birth = request.POST['date_of_birth']
        aadharnumber = request.POST['aadharnumber']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        bloodgroup = request.POST['bloodgroup']
        # dropdown = request.POST['dropdown']
        address = request.POST['address']
        symptoms = request.POST['symptoms']

        ename = request.POST['ename']
        relation = request.POST['relation']
        emergencynumber = request.POST['emergencynumber']
        
        ins = Patient(fname=fname, lname=lname, gender=gender, date_of_birth=date_of_birth, aadharnumber=aadharnumber, email=email, phonenumber=phonenumber, 
        bloodgroup=bloodgroup, address=address, symptoms=symptoms, ename=ename, relation=relation, emergencynumber=emergencynumber)
        ins.save()
    return render(request, 'patient.html', {})

def Doctordetails(request):
    if request.method == "POST":
        dname = request.POST['dname']
        specialization = request.POST['specialization']
        gender = request.POST['gender']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        
        ins = Doctor(dname=dname, specialization=specialization, gender=gender,email=email, phonenumber=phonenumber)
        ins.save()
    return render(request,'Doctor1.html', {})

def Doctor_information(request):
    # Query the database to retrieve all DoctorInformation objects
    doctors = Doctor.objects.all()

    # Pass the retrieved data to the template
    context = {'doctors': doctors}
    return render(request, 'doctor_information.html', context)

















def Priscription(request):
    # Fetch only approved appointments
    approved_appointments = Apps.objects.filter(is_approved=True)

    context = {'approved_appointments': approved_appointments}
    return render(request, 'Priscription.html', context)


@login_required
def profile_view(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        return render(request, 'Priscription.html', {'user_profile': user_profile})
    except UserProfile.DoesNotExist:
        # Handle the case when the UserProfile does not exist for the current user
        user_profile = UserProfile.objects.create(user=request.user, additional_data="Default Data")
        return render(request, 'Priscription.html', {'user_profile': user_profile})

def create_profile_view(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        phno = request.POST.get('number')
        password = request.POST.get('password')

        new_user = User.objects.create_user(name, email, password)
        new_user.phno = phno

        new_user.save()
        return redirect('create_profile')
    return render(request, 'create_profile.html')


def Appointment_System(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        phoneNo = request.POST.get('phoneNo')
        appointment = request.POST.get('appointment')
        symptoms = request.POST.get('symptoms')

        new_appointment = Apps.objects.create(
            name=name,
            age=age,
            phoneNo=phoneNo,
            appointment=appointment,
            symptoms=symptoms
        )

        # You can add additional logic here if needed

        return redirect('appointment1')

    return render(request, 'appointment1.html', {})


def appointment_list(request):
    # Fetch only approved appointments
    approved_appointments = Apps.objects.filter(is_approved=True)

    context = {'approved_appointments': approved_appointments}
    return render(request, 'appointment_list.html', context)