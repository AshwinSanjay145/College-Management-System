from django.db import models

# Create your models here.
class students(models.Model):
    firstname=models.CharField(max_length=200) 
    lastname=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    department=models.CharField(max_length=200)
    reg_no=models.CharField(max_length=8)
    semaster=models.CharField(max_length=2)
    password1=models.CharField(max_length=200,null=True)
    password2=models.CharField(max_length=200,null=True)
    gender= models.CharField(max_length=200,null=True)
    place= models.CharField(max_length=200,null=True)
    guardian_phone = models.CharField(max_length=10,null=True)
    image = models.ImageField(null=True,blank=True,upload_to ="images/")


class teachers(models.Model):
    firstname=models.CharField(max_length=200) 
    lastname=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    department=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    id_no=models.CharField(max_length=4)
    password1=models.CharField(max_length=200,null=True)
    password2=models.CharField(max_length=200,null=True)
    gender= models.CharField(max_length=200,null=True)
    contact_no = models.CharField(max_length=10,null=True)
    image = models.ImageField(null=True,blank=True,upload_to ="images/")

class principal(models.Model):
    firstname=models.CharField(max_length=200) 
    lastname=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    id_no=models.CharField(max_length=4)
    password1=models.CharField(max_length=200,null=True)
    password2=models.CharField(max_length=200,null=True)
    gender= models.CharField(max_length=200,null=True)
    contact_no = models.CharField(max_length=10,null=True)
    image = models.ImageField(null=True,blank=True,upload_to ="images/")


class s1(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    reg_no=models.CharField(max_length=8)
    physics=models.CharField(max_length=8)
    chemistry=models.CharField(max_length=8)
    mathematics=models.CharField(max_length=8)
    graphics=models.CharField(max_length=8)
    electronics=models.CharField(max_length=8)
    p_res=models.CharField(max_length=200,null=True)
    c_res=models.CharField(max_length=200,null=True)
    e_res=models.CharField(max_length=200,null=True)
    m_res=models.CharField(max_length=200,null=True)
    g_res=models.CharField(max_length=200,null=True)
    sem=models.CharField(max_length=200,null=True)


class leave(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    department=models.CharField(max_length=200)
    semester=models.CharField(max_length=10)
    days=models.CharField(max_length=10,null=True)
    fromdate=models.DateField()
    todate=models.DateField()
    reason=models.CharField(max_length=200)
    desp=models.TextField()
    reg_no=models.CharField(max_length=8,null=True)

class notes(models.Model):
    name=models.CharField(max_length=200)
    department=models.CharField(max_length=30)
    semester=models.CharField(max_length=10)
    subject=models.CharField(max_length=30,null=True)
    upload_date=models.CharField(max_length=20,null=True)
    filetype=models.CharField(max_length=30)
    file=models.FileField(null=True,upload_to='media/')
    status=models.CharField(max_length=30)
    session=models.CharField(max_length=30)
    reg_no=models.CharField(max_length=8,null=True)

class notices(models.Model):
    todaydate=models.CharField(max_length=20)
    todaytime=models.CharField(max_length=20)
    lastdate=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    session=models.CharField(max_length=10)
    content=models.TextField(max_length=500)


