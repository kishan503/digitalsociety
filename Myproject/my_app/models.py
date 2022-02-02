from django.db import models

# Create your models here.
class user(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    role=models.CharField(max_length=50)
    email=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=100)
    otp=models.IntegerField(default=7812)
class s_member(models.Model):
    flat_no=models.CharField(max_length=10,null=True)
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    email=models.CharField(max_length=100,unique=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    dob=models.CharField(max_length=15,null=True)
    gender=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)
    country=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=100,null=True)
    phone_number=models.CharField(max_length=10,null=True)
    pincode=models.CharField(max_length=10,null=True)
class watchman(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    email=models.CharField(max_length=100,unique=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    dob=models.CharField(max_length=15,null=True)
    gender=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)
    country=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=100,null=True)
    phone_number=models.CharField(max_length=10,null=True)
    pincode=models.CharField(max_length=10,null=True)
class chairman(models.Model):
    flat_no=models.CharField(max_length=10,null=True)
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    email=models.CharField(max_length=100,unique=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    dob=models.CharField(max_length=15,null=True)
    gender=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)
    country=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=100,null=True)
    phone_number=models.CharField(max_length=10,null=True)
    pincode=models.CharField(max_length=10,null=True)
class visitor(models.Model):
    name=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=50)
    flat_no=models.CharField(max_length=50)
    date=models.DateField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)
class comp_details(models.Model):
    email=models.CharField(max_length=100)
    flat_no=models.CharField(max_length=10)
    c_subject=models.CharField(max_length=50)
    c_discription=models.CharField(max_length=150)
class sugg_details(models.Model):
    email=models.CharField(max_length=100)
    flat_no=models.CharField(max_length=10)
    s_subject=models.CharField(max_length=50)
    s_discription=models.CharField(max_length=150)
class notice_details(models.Model):
    name=models.CharField(max_length=50)
    n_subject=models.CharField(max_length=100)
    n_discription=models.CharField(max_length=250)
    n_date=models.DateField(auto_now_add=True)
class event_details(models.Model):
    m_name=models.CharField(max_length=50)
    e_name=models.CharField(max_length=50)
    e_date=models.CharField(max_length=50)
    e_discription=models.CharField(max_length=50)
    date=models.DateField(auto_now_add=True)
class gallary(models.Model):
    user_id = models.ForeignKey(user,on_delete=models.CASCADE)
    picture = models.FileField(upload_to='media/images/',blank=True,null=True)
    
    def __str__(self):
        return self.user_id.first_name