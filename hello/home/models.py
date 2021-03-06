from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()


    def __str__(self):
        return self.name



class Stforms(models.Model):
    fname=models.CharField(max_length=120)
    lname=models.CharField(max_length=120)
    email=models.EmailField(max_length=50)
    contact_number=models.CharField(max_length=20)
    aadhar_number = models.CharField(max_length=20)
    
    category = models.CharField(max_length=10)
    dob = models.DateField()
    gender = models.CharField(max_length=7)
    boeHs = models.CharField(max_length=7)
    yearHs = models.CharField(max_length=4)
    resultHs = models.CharField(max_length=10)
    boeGd = models.CharField(max_length=7)
    yearGd = models.CharField(max_length=4)
    resultGd = models.CharField(max_length=10)
    course = models.CharField(max_length=10,default='')
   
   
    mothna = models.CharField(max_length=120)
    mothc = models.CharField(max_length=120)
    motho = models.CharField(max_length=120)
    fathna = models.CharField(max_length=120)
    fathc = models.CharField(max_length=120)
    fatho = models.CharField(max_length=120)
    ques = models.CharField(max_length=13)
    add1 = models.CharField(max_length=120)
    add2 = models.CharField(max_length=120)
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    pincode = models.CharField(max_length=20)
    padd1 = models.CharField(max_length=120)
    padd2 = models.CharField(max_length=120)
    pcountry = models.CharField(max_length=120)
    pstate = models.CharField(max_length=120)
    pcity = models.CharField(max_length=120)
    ppincode = models.CharField(max_length=120)
    
    photo = models.FileField(upload_to='images/')
    sign = models.FileField(upload_to='images/')
    Hsmark = models.FileField(upload_to='images/')
    certiHs = models.FileField(upload_to='images/')
    Gdmark = models.FileField(upload_to='images/')
    certiGd = models.FileField(upload_to='images/')
    
    
    

    def __str__(self):
        return self.fname



    
