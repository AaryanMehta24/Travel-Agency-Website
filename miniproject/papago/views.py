from django.http.response import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from .models import DestinationDetails, TravelDetails, TravellerDetails, PaymentDetails
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# from .models import Destination
# Create your views here.

def home(request):
    return render(request,'index.html')

def packages(request):
    return render(request,'packages.html')

def login(request):
    return render(request,'login.html')


@login_required(login_url='login')
def booking(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        print(user_id)
        return render(request,'booking.html')
    return render(request,'index.html')


@login_required(login_url='login')
def traveller(request):
    if request.user.is_authenticated and request.method=='POST':
        # if request.method=='POST':

            destination_selected= request.POST['destination_options']
            child = request.POST['child']
            adult = request.POST['adult']
            infant = request.POST['infant']
            date = request.POST['dateofarrival']
            
            #To fetch user_id of logged-in user
            userid = request.user.id
            

            #To fetch des_id from DestinationDetails table
            # print(destination_selected)
            des_details= DestinationDetails.objects.get(des_name=destination_selected)
            desid =des_details.des_id
            print(des_details.des_id)
            print(userid)
            print(child)
            print(adult)
            print(infant)
            print(date)


            bookingdata = TravelDetails(total_adults=adult,total_child=child,total_infant=infant,travel_date=date,des_id_id=desid,user_id_id=userid)
            
            bookingdata.save();
            print('saved')
            return render(request,'traveller.html')
    else:
        return render(request,'traveller.html')
    
    # else:   
    #     return render(request,'traveller.html')

def register(request):
    return render(request,'register.html')

@login_required(login_url='login')
def payment(request):
    # userid = request.user.id
    # if request.user.is_authenticated and request.method=="POST":
    #     # destination = request.POST['destination']
    #     amt = request.POST.get('amount')
    #     mode = request.POST.get('paymentmode')
        
    #     paymentdata = PaymentDetails(payment_mode=mode,payment_amount=amt,user_id_id=userid)
    #     paymentdata.save();

    #     return render(request,'index.html')
    # else:
        return render(request,'payment.html')


def addPayment(request):
    userid = request.user.id
    if request.method=="POST":
        user_traveldetails = TravelDetails.objects.get(user_id_id=userid)
        desid = user_traveldetails.des_id_id
        adultno = user_traveldetails.total_adults
        childno = user_traveldetails.total_child
        infantno = user_traveldetails.total_infant
        adult_int=int(adultno)
        child_int=int(childno)
        infant_int=int(infantno)
        
        des_details = DestinationDetails.objects.get(des_id=desid)
        priceadult=des_details.price_adult
        pricechild=des_details.price_child
        priceinfant=des_details.price_infant
        
        adultprice=int(priceadult)
        childprice=int(pricechild)
        infantprice=int(priceinfant)
        
        adult_total= adult_int*adultprice
        child_total= child_int*childprice
        infant_total= infant_int*infantprice

        total_amount= adult_total+child_total+infant_total


        
        
        destinationselected=request.POST.get('destination')
        amt = request.POST.get('amount')
        mode = request.POST.get('paymentmode')
        print(destinationselected)
        print(amt)
        print(mode)
        print(userid)
        paymentdata = PaymentDetails(payment_mode=mode,payment_amount=total_amount,user_id_id=userid)
        paymentdata.save();

        return render(request,'index.html')
    else:
        return render(request,'payment.html')

def registerUser(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        #If passwords match then only the block will be executed
        if password1==password2:
        
            try:
                #Checking if username is already registered
                user = User.objects.get(username=username)
                messages.info(request,'Username Taken')  
                return render(request,'register.html')
            except User.DoesNotExist:
                try:
                    #Checking if email is already registered
                    user = User.objects.get(email=email)
                    messages.info(request,'Email already registered to an account')
                    return render(request,'register.html')
                except User.DoesNotExist:
                    #Saving the entered data into the database table
                    user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password1,email=email)
                    user.save();
                    
                    messages.success(request,'Registration Successful!!')
                    return render(request,'login.html')
                    

        else:
            messages.error(request,'Passwords do not match')
            return render(request,'register.html')
    else:
        return render(request,'register.html')
                

    #     if password1==password2:
    #         if User.objects.filter(username=username).exists():
    #             raise ValueError("Username exists!")
                
    #         elif User.objects.filter(email=email).exists():

    #             raise ValueError("Email already registered to an account!")
    #         else:

    #             user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password1,email=email)
    #             user.save();
    #             print('User created')
    #             return render(request,'login.html')
    #     else:
            
    #         return render(request,'register.html')

        
        
        

    # else:
    #     return render(request,'index.html')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password3 = request.POST.get('password3')

        user = auth.authenticate(username=username,password=password3)

        if user is not None:
            auth.login(request, user)
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            messages.success(request,'Login Successful')
            return render(request,'index.html')
        else:
            messages.error(request,'Invalid Credentials')
            return render(request,'login.html')
            
    else:
        return render(request,'index.html')

def logout(request):
    auth.logout(request)
    return render(request,'index.html')


def create(request):
    userid = request.user.id
    if request.method=='POST':
        name=request.POST['travellername']
        age = request.POST['travellerage']
        travel = TravelDetails(traveller_age=age,traveller_name=name,user_id_id=userid)
        travel.save()
        return HttpResponse('')