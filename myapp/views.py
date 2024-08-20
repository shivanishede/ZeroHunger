from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.http import JsonResponse
from datetime import datetime
from django.utils import timezone
from django.db import IntegrityError
from .models import DonarInfo  
from datetime import date

def success(request):
    return render(request, 'success.html')
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

# def signup_view(request):
#     return render(request, 'signup.html')

def login_view(request):
    return render(request, 'login.html')

def information_view(request):
    return render(request, 'information.html')
# def receiver_view(request):
#     return render(request, 'register.html')

def signup_view(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        # phno= request.POST['phno']
        email = request.POST['email']
        password = request.POST['password']

        try:
            # Create a new user instance with hashed password
            user = User.objects.create(
                first_name=fname,
                last_name=lname,
                # phone_number=phno,
                email=email,
                password=make_password(password)  # Hashing password
            )
            
            # Redirect to the login page after successful registration
            return redirect('login')

        except IntegrityError:
            # Handle integrity error (e.g., display error message)
            pass

    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        password = request.POST.get('password')

        try:
           
            user = User.objects.get(first_name=firstname)
            
            if check_password(password, user.password):
                
                return redirect('information')
            else:
                
                return render(request, 'login.html', {'error_message': 'Invalid first name or password.'})

        except User.DoesNotExist:
           
            return render(request, 'login.html', {'error_message': 'Invalid first name or password.'})

    return render(request, 'login.html')

def logout_view(request):
    return render(request, 'logout.html')

def donar_view(request):
    return render(request, 'donar.html')

def receiver_view(request):
    return render(request, 'receiver.html')


def donarinfo(request):
    return render(request, 'donarinfo.html')

def donarview(request):
    return render(request, 'donarview.html')

def deletedonar(request):
    return render(request, 'deletedonar.html')

def editdonar(request, donar_id):
    donar_info =get_object_or_404(DonarInfo,pk=donar_id) 
    
    return render(request, 'editdonar.html', {'donar_info': donar_info})
def save_donar_info(request, donor_id):
    donor = get_object_or_404(DonarInfo, pk=donor_id)
    if request.method == 'POST':
        form = DonarInfo(request.POST, instance=donor)  # Use DonarInfoForm
        if form.is_valid():
            form.save()
            return redirect('donarinfo')  
    else:
        form = DonarInfo(instance=donor)  # Use DonarInfoForm
    return render(request, 'editdonar.html', {'form': form})

def submit_donar_info(request):
    if request.method == 'POST':
        # Retrieve data from POST request
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        address = request.POST.get('address')
        date = request.POST.get('date')
        mobileno = request.POST.get('mobileno')
        email = request.POST.get('email')
        pincode = request.POST.get('pincode')
        expiry = request.POST.get('expiry')

        # Save the data to the database
        donar_info = DonarInfo.objects.create(
            name=name,
            quantity=quantity,
            address=address,
            date=date,
            mobileno=mobileno,
            email=email,
            pincode=pincode,
            expiry=expiry
        )

        # Redirect to a success page
        return redirect('success')
    else:
        # If the request method is not POST, return an error
        return JsonResponse({'error': 'Invalid request method'}, status=400)

def donarview(request):
    # Retrieve all donor information from the database
    donar_info = DonarInfo.objects.all()

    # Pass the donor information to the template context
    return render(request, 'donarview.html', {'donar_info': donar_info})

def receiverview(request):
   
    # donar_info = DonarInfo.objects.all()
    today = date.today()
    donar_info = DonarInfo.objects.filter(expiry__gte=today) 

    return render(request, 'receiverview.html', {'donar_info': donar_info})

def deletedonar(request):
    if request.method == 'GET':
        donor_id = request.GET.get('id')
        donor = get_object_or_404(DonarInfo, id=donor_id)
        donor.delete()
        # Redirect to a success page or return a success message
        return redirect('donarview')

def certificate(request, donar_id):
    donar_info =get_object_or_404(DonarInfo,pk=donar_id) 
    return render(request, 'certificate.html', {'donar_info': donar_info})


# def submit_donation(request):
#     if request.method == 'POST':
#         form = DonationForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the form data to the database
#             return redirect('success_page')  # Redirect to a success page
#     else:
#         form = DonationForm()
#     return render(request, 'donar.html', {'form': form})
