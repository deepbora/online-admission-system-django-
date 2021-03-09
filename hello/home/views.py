from django.shortcuts import render , HttpResponse,redirect
from django.conf import settings
from datetime import datetime
from home.models import Contact
from home.models import  Stforms
from django.template import loader
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session

# Create your views here.
def index(request):
 

    if request.session.has_key('is_logged'):
         logout(request)
           

 
    else: 
         return redirect('login')


def formpage(request):
    if request.session.has_key('is_logged'):
        

    

        if request.method == "GET":
                return render(request,'forms.html')
        elif request.method == "POST":
                fname=request.POST.get('fname')
                lname=request.POST.get('lname')
                email=request.POST.get('email')
                contact_number=request.POST.get('cno')
                aadhar_number = request.POST.get('ano')
                
                category = request.POST.get('cat')
                dob = request.POST.get('dob')
                gender = request.POST.get('gen')
                boeHs = request.POST.get('boe')
                yearHs = request.POST.get('yop')
                resultHs = request.POST.get('res')
                boeGd = request.POST.get('boe')
                yearGd = request.POST.get('yop')
                resultGd = request.POST.get('res')
                course = request.POST.get('cour')
                
                
                mothna = request.POST.get('mna')
                mothc = request.POST.get('mno')
                motho = request.POST.get('mo')
                fathna = request.POST.get('fna')
                fathc = request.POST.get('fno')
                fatho = request.POST.get('fo')
                ques = request.POST.get('ind')
                add1 = request.POST.get('ad1')
                add2 = request.POST.get('ad2')
                country = request.POST.get('con')
                state = request.POST.get('state')
                city = request.POST.get('city')
                pincode = request.POST.get('pc')
                padd1 = request.POST.get('pad1')
                padd2 = request.POST.get('pad2')
                pcountry = request.POST.get('pcon')
                pstate = request.POST.get('pstate')
                pcity = request.POST.get('pcity')
                ppincode = request.POST.get('ppc')
                
                photo = request.FILES['pic']
                sign = request.FILES['sign']
                Hsmark = request.FILES['mark']
                certiHs = request.FILES['mark']
                Gdmark =  request.FILES['mark']
                certiGd = request.FILES['mark']
                
                form_instance= Stforms(fname=fname,lname=lname, email=email,contact_number=contact_number,aadhar_number=aadhar_number,category=category,dob=dob,gender=gender,boeHs=boeHs,yearHs=yearHs,resultHs=resultHs,boeGd=boeGd,yearGd=yearGd,resultGd=resultGd,course=course,mothna=mothna,mothc=mothc,motho=motho,fathna=fathna,fathc=fathc,fatho=fatho, ques= ques, add1=add1,add2=add2,country=country,state=state,city=city,pincode=pincode,padd1=padd1,padd2=padd2,pcountry=pcountry,pstate=pstate,pcity=pcity,ppincode=ppincode,photo=photo,sign=sign,Hsmark=Hsmark,certiHs=certiHs,Gdmark=Gdmark,certiGd=certiGd)
                form_instance.save()
                
                    #return render(request,'reg2.html',{'forms':form_instance})
                    #return HttpResponse("<h3>Successfullty Registered</h3>")
                messages.error(request,'Succesfully Submitted Youre form!!! We will be communicated shortly!!')
        return redirect('login')
    else:
        return redirect('error')

 


    
@login_required(login_url='login')
def admin(request):
 
 
    return render(request,'admin.html')





def loginpage(request):

    if request.session.has_key('is_logged'):
         logout(request)
           
 
        
    
    elif request.method=='POST':
       username=request.POST.get('username')
       password=request.POST.get('password')
       user=authenticate(request,username=username,password=password)
       if user is not None:
           login(request,user)
           request.session['is_logged']=True
           return redirect('student')
                   
       else:
            messages.info(request,"Username OR Paswword Incorect")     
      
           


    return render(request,'login.html')
    

def register(request):
    if request.session.has_key('is_logged'):
         logout(request)
    else:  
    
   
        form=CreateUserForm()

        if request.method=='POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
            
                messages.success(request, 'Your account is succsefully created!!')
                return redirect('login')


        context={'form':form}
    
        return render(request,'register.html',context)
    
        
def logoutUser(request):
    logout(request)
    return redirect('login')   

   

      



def cours(request):

    if request.session.has_key('is_logged'):
         logout(request)
    else:  
    #return HttpResponse("this is cours page")
         return render(request,'cours.html')


def about(request):
    #return HttpResponse("this is about page")
    return render(request,'about.html')

def contact(request):
    
    if request.session.has_key('is_logged'):
         logout(request)



    elif request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your massage has been sent!')
       

   # return HttpResponse("this is contect page")
    return render(request,'contact.html')  


def student(request):

    if request.session.has_key('is_logged'):
        return render(request,'student.html')


    else:
    
    #return HttpResponse("this is cours page")
         return render(request,'error.html')


def error(request):
    return render(request,'error.html')


