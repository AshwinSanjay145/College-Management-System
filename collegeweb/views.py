from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login as log,logout
from django.contrib import messages
from .forms import s_form,t_form,p_form,s_upnotes
from .models import principal,students,teachers,s1,leave,notes,notices
from django.core.mail import send_mail #
from .forms import *

from datetime import datetime,date



# Create your views here.

today = date.today()
today = today.strftime("%d-%b-%Y")
now = datetime.now()
t = now.strftime("%H:%M")
print(today)
print(t)

def index(request):
    return render(request,"index.html")

def admin(request):
    return render(request,"ad_login.html")

def super(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            return redirect(adlog)
        else:
            messages.success(request,"Admin Check Username and Password")
            return render(request,'ad_login.html')
    else:
        return render(request,'home.html')
    
def adlog(request):
    return render(request,"ad_log.html")

def a_logout(request):
    logout(request)
    messages.success(request,("End of session"))
    return redirect(admin)

def ad_student(request):
    form = s_form()
    if request.method=='POST':
        form = s_form(request.POST,request.FILES)
        p1 = request.POST.get('password1')
        p2 = request.POST.get('password2')
        email = request.POST.get('email')
        reg = request.POST.get('reg_no')
        print(email)
        print(reg)
        f=request.POST.get('firstname')
        l=request.POST.get('lastname')
        name= f +" " +l
        print(name)
        if form.is_valid():
            if p1==p2:
                
                send_mail(
                'Profile Created', #subject
                'hi ' +name+ ', this is to inform that your student profile has been created'
                ' Register Number :' + reg +
                ' Password :'+ p1 +
                ' kindly login and change password ',

                'ashwinspanicker@gmail.com',
                [email],
                fail_silently=False,
                )
                form.save()
                messages.success(request,"Student Registered Succesfully")

            else:
                messages.success(request,"Password Mismatched")
            
    return render(request,'ad_student.html',{'form':form})

def add_student(request):
    return render(request,"ad_student.html")


def ad_teacher(request):
    form = t_form()
    if request.method=='POST':
        form = t_form(request.POST,request.FILES)
        p1 = request.POST.get('password1')
        p2 = request.POST.get('password2')
        email = request.POST.get('email')
        id = request.POST.get('id_no')
        print(email)
        print(id)
        f=request.POST.get('firstname')
        l=request.POST.get('lastname')
        d=request.POST.get('department')
        s=request.POST.get('subject')
        name= f +" " +l
        print(name)
        if form.is_valid():
            if p1==p2:
                send_mail(
                'Profile Created', #subject
                'hi ' +name+ ', this is to inform that your Teacher profile has been created for Department : ' + d + ', Subject : ' + s +
                ', ID Number : ' + id +
                ', Password : '+ p1 +
                '. kindly login and change password ',

                'ashwinspanicker@gmail.com',
                [email],
                fail_silently=False,
                )
                form.save()
                messages.success(request,"Teacher Profile Created")
                

            else:
                messages.success(request,"Password Mismatched")
            
    return render(request,'ad_teacher.html',{'form':form})

def p_update(request):
    form = p_form()
    if request.method=='POST':
        form = p_form(request.POST,request.FILES)
        id = request.POST.get('id_no')
        p1 = request.POST.get('password1')
        p2 = request.POST.get('password2')
        f=request.POST.get('firstname')
        l=request.POST.get('lastname')
        email=request.POST.get('email')
        
        name= f +" " +l
        print(id)
        if form.is_valid():
            if p1==p2:
                
                send_mail(
                'Profile Created', #subject
                'hi '+name+ ', this is to inform that your Prinicpal profile has been created for ST THOMAS College' +
                ', ID Number : ' + id +
                ', Password : '+ p1 +
                '. kindly login and change password ',

                'ashwinspanicker@gmail.com',
                [email],
                fail_silently=False,
                )
                form.save()
                messages.success(request,"Principal Updated Succesfully")
                cr = principal.objects.filter(id_no=id)
            else:
                messages.success(request,"Password Mismatched")
            
    return render(request,'ad_principal.html',{'form':form})

def s_view(request):
    cr = students.objects.all()
    return render(request,"ad_s_view.html",{'cr':cr})

def s_delete(request,pk):
    cr=students.objects.get(id=pk)
    cr.delete()
    messages.success(request," Removed successfully")
    return redirect(s_view)

def p_delete(request,pk):
    cr=principal.objects.get(id=pk)
    cr.delete()
    messages.success(request," Removed successfully")
    return redirect(p_view)

def t_view(request):
    pr = teachers.objects.all()
    return render(request,"ad_t_view.html",{'pr':pr})

def p_view(request):
    cr = principal.objects.all()
    return render(request,"ad_p_view.html",{'cr':cr})



# ***** Student Session ****



def s_login(request):
    return render(request,"s_login.html")

def s_check(request):
    today = date.today()
    today = today.strftime("%d-%b-%Y")
    now = datetime.now()
    t = now.strftime("%H:%M")
    print(today)
    print(t)
    
    if request.method == "POST":
        regno = request.POST.get('regno')
        password = request.POST.get('password')
        cr = students.objects.filter(reg_no=regno, password1=password)
        if cr:
            user_details=students.objects.get(reg_no=regno,password1=password)
            cr=user_details
            reg=user_details.reg_no
            pswd=user_details.password1
            name=user_details.firstname
            email=user_details.email
            request.session['sreg']=reg
            request.session['spswd']=pswd

            send_mail(
                'Login', #subject
                'hi ' +name+ ', Your successfully login. ' + 'Time :' +t+ ", Date " + today,
                'ashwinspanicker@gmail.com',
                [email],
                fail_silently=False,
            )
            messages.success(request,"There are some notifications for you")
            return redirect(s_log)
               
        else:
            messages.success(request,"login unsuccessfull :( ")
            return render(request,'s_login.html')
    
    else:
        return render(request,'s_login.html')



def s_logout(request):
    logout(request)
    messages.success(request,("You were Signed out"))
    return redirect(s_login)

def s_log(request):
    reg=request.session['sreg']
    print(reg)
    pswd=request.session['spswd']
    user_details=students.objects.get(reg_no=reg,password1=pswd)
    cr=user_details
    
    notice=notices.objects.all().order_by('-id').values()
    nr=notice
    return render(request,'s_log.html',{'cr':cr,'msg':nr})

def s_notify(request):
    reg=request.session['sreg']
    pswd=request.session['spswd']
    user_details=students.objects.get(reg_no=reg,password1=pswd)
    cr=user_details
    
    notice=notices.objects.all().order_by('-id').values()
    nr=notice
    return render(request,'s_notification.html',{'cr':cr,'msg':nr})

def s_marklist(request):
    
    reg=request.session['sreg']
    cr=students.objects.get(reg_no=reg)
    
    marklist=s1.objects.get(reg_no=reg)
    mr=marklist
    print(mr.physics)
    if cr and mr:
        print(mr)
        return render(request,"s_marklist.html",{'cr':cr,'pr':mr})
    else:
        messages.success(request,"Marklist upload pending")
        return render(request,"s_marklist.html",{'cr':cr,'pr':mr})
    
        

def s_profile(request):
    reg=request.session['sreg']
    pr=s1.objects.get(reg_no=reg)
    cr=students.objects.get(reg_no=reg)
    return render(request,"s_profile.html",{'cr':cr,'pr':pr})
    
def s_pro_update(request):
    reg=request.session['sreg']
    pswd=request.session['spswd']
    cr = students.objects.get(reg_no=reg,password1=pswd)
    profile=cr
    f=profile.firstname
    l=profile.lastname
    name=f + " " + l
    pswd=profile.password1
    email=profile.email
    print(email)
    
    form = s_p_p_form(instance=cr)
    if request.method=="POST":
        old=request.POST.get("old")
        print(old)
        p1=request.POST.get("password1")
        p2=request.POST.get("password2")
        if old==pswd:
            if p1==p2:
                form = s_p_p_form(request.POST,instance=cr)
                if form.is_valid:
                    send_mail(
                    'Password Changed', #subject
                    'hi '+name+ ', your password is updated and you were signed out please sign in again.' +
                    
                    ' kindly login and check password ',

                    'ashwinspanicker@gmail.com',
                    [email],
                    fail_silently=False,
                    )
                    form.save()
                    messages.success(request,"Password updated Sign in again")
                    return redirect(s_logout)
                else:
                    messages.success(request,"Entered Passwords Mismatched")      
        else:
            messages.success(request,"Oops Incorrect old Password")
                
    return render(request,"s_profile_update.html",{'form':form,'cr':cr})

def s_pro_update2(request):
    reg=request.session['sreg']
    pswd=request.session['spswd']
    cr = students.objects.get(reg_no=reg,password1=pswd)
    profile=cr
    pswd=profile.password1
    print(pswd)
    
    
    f=profile.firstname
    l=profile.lastname
    name=f + " " + l
    form = s_p_e_form(instance=cr)
    if request.method=="POST":
        old=request.POST.get("old")
        email=request.POST.get("email")
        print(email)
        if old==pswd:
            form = s_p_e_form(request.POST,instance=cr)
            if form.is_valid:
                send_mail(
                'Email Updated', #subject
                'hi '+name+ ', your profile Email is updated' +
                    
                ' kindly verify your new email :' + email,

                'ashwinspanicker@gmail.com',
                [email],
                fail_silently=False,
                )
                form.save()
                messages.success(request,"New Email Updated and Confirmation mail has sent ")
            
                  
        else:
            messages.success(request,"Oops Incorrect old Password")
                
    return render(request,"s_p_email.html",{'form':form,'cr':cr})



def s_leave(request):
    reg=request.session['sreg']
    print(reg)
    user_details=students.objects.get(reg_no=reg)
    cr=user_details
    return render(request,"s_leave.html",{'cr':cr})

    
def s_add_leave(request):
    if request.method=="POST":
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        department = request.POST.get('dept')
        sem = request.POST.get('sem')
        frm= request.POST.get('fdate')
        to = request.POST.get('tdate')
        reason = request.POST.get('reason')
        desp = request.POST.get('desp')
        days = request.POST.get('day')
        print(desp)
        print(firstname)
        leave(firstname=firstname,lastname=lastname,department=department,semester=sem,fromdate=frm,todate=to,reason=reason,desp=desp,days=days).save()
        messages.success(request,"Leave Submitted")
        return redirect(s_leave) 

def s_notes(request):
    reg=request.session['sreg']
    pswd=request.session['spswd']
    cr = students.objects.get(reg_no=reg,password1=pswd)
    today = date.today()
    t = today.strftime("%d-%b-%Y")
    print(t)
    reg=request.session['sreg']
    user_details=students.objects.get(reg_no=reg)
    name=user_details.firstname+" "+user_details.lastname
    intial_data={
        "name":name,
        "department":user_details.department,
        "semester":user_details.semaster,
        "upload_date":t

    }
    form=s_upnotes(initial=intial_data)
    mydict={
        'form':form,
        'cr':cr,
    }
    
    
    if request.method =='POST':
        sub=request.POST.get('subject')
        sess=request.POST.get('session')
        
        msg = name+" your "+ sess + " has been Submiited to "+ sub +" " +"lecturer"
        form = s_upnotes(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,msg)

    return render(request,"s_uploadfile.html",context=mydict)


     
        
    


# ***** teacher sessions *****



def t_login(request):
    return render(request,"t_login.html")



def t_check(request):

    if request.method == "POST":
        idno = request.POST.get('idno')
        password = request.POST.get('password')
        cr = teachers.objects.filter(id_no=idno, password1=password)
        if cr:
            user_details=teachers.objects.get(id_no=idno,password1=password)
            cr=user_details
            f=cr.firstname
            l=cr.lastname
            name=f + " " + l
            idno=user_details.id_no
            pswd=user_details.password1
            
            email=user_details.email
            request.session['tidno']=idno
            request.session['tpswd']=pswd
            

            send_mail(
                'Login', #subject
                'hi ' +name+ ', Your successfully login. ' + 'Time :' +t+ ", Date " + today,
                'ashwinspanicker@gmail.com',
                [email],
                fail_silently=False,
            )
            
            return redirect(t_log)
        

        else:
            messages.success(request,"Check Your ID and Password !")
            return render(request,'t_login.html')
    
    else:
        return render(request,'t_login.html')

def t_logout(request):
    logout(request)
    messages.success(request,("you were Signed out"))
    return redirect(t_login)


def t_loghome(request):
    idno=request.session['tidno']
    pswd=request.session['tpswd']
    user_details=teachers.objects.get(id_no=idno,password1=pswd)
    cr=user_details
    return render(request,"t_loghome.html",{'cr':cr})

def t_log(request):
    idno=request.session['tidno']
    pswd=request.session['tpswd']
    user_details=teachers.objects.get(id_no=idno,password1=pswd)
    cr=user_details
    
    sub=user_details.subject
    pswd=user_details.password1
    request.session['sub']=sub
    request.session['pswd']=pswd
    print(idno)
    print(pswd)
    return render(request,'t_log.html',{'cr':cr})
    
def t_upmark(request):
    return render(request,"t_upmark.html")

def t_uploadmark(request):
    idno=request.session['tidno']
    pswd=request.session['tpswd']
    user_details=teachers.objects.get(id_no=idno,password1=pswd)
    cr=user_details
    if request.method=="POST":
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        regno = request.POST.get('regno')
        rec = s1.objects.filter(reg_no=regno,firstname=firstname,lastname=lastname)
        student_details = students.objects.filter(reg_no=regno,firstname=firstname,lastname=lastname)
        pc=student_details
        print(regno)
        if pc:
            if rec:
                messages.success(request,"Student already exist")
            else:
                s1(firstname=firstname,lastname=lastname,reg_no=regno,).save()  
                messages.success(request,"Student added successfully") 
        else:
            messages.success(request,"Student doesn't exist..! ")
    return render(request,"t_upmark.html",{'cr':cr})

def t_updatemark(request):
    return render(request,"t_updatemark.html")



def t_profile_update(request):
    idno=request.session['tidno']
    pswd=request.session['tpswd']
    user_details=teachers.objects.get(id_no=idno,password1=pswd)
    pk=user_details.subject
    cr = teachers.objects.get(subject=pk)
    profile=cr
    pswd=profile.password1
    email=profile.email
    print(pswd)
    f=profile.firstname
    l=profile.lastname
    name=f + " " + l
    form = t_p_form(instance=cr)
    if request.method=="POST":
        old=request.POST.get("old")
        print(old)
        p1=request.POST.get("password1")
        p2=request.POST.get("password2")
        if old==pswd:
            if p1==p2:
                form = t_p_form(request.POST,instance=cr)
                if form.is_valid:
                    send_mail(
                    'Password Changed', #subject
                    'hi '+name+ ', your password is updated and you were signed out please sign in again.' +
                    
                    ' kindly login and check password ',

                    'ashwinspanicker@gmail.com',
                    [email],
                    fail_silently=False,
                    )
                    form.save()
                    messages.success(request,"Password updated Sign in again")
                    logout(request)
                    return redirect(t_login)
                else:
                    messages.success(request,"Entered Passwords Mismatched")      
        else:
            messages.success(request,"Oops Incorrect old Password")
                
    return render(request,"t_profile_update.html",{'form':form,'cr':cr})

def t_profile_update2(request):
    idno=request.session['tidno']
    pswd=request.session['tpswd']
    user_details=teachers.objects.get(id_no=idno,password1=pswd)
    pk=user_details.subject
    cr = teachers.objects.get(subject=pk)
    profile=cr
    pswd=profile.password1
    
    p1=profile.password1
    print(pswd)
    f=profile.firstname
    l=profile.lastname
    name=f + " " + l
    form = t_p_e_form(instance=cr)
    if request.method=="POST":
        old=request.POST.get("old")
        email=request.POST.get("email")
        print(email)

        
        if old==p1:
            form = t_p_e_form(request.POST,instance=cr)
            if form.is_valid:
                send_mail(
                    'Email Updated', #subject
                    'hi '+name+ ', your profile Email is updated' +
                        
                    ' kindly verify your new email :' + email,

                    'ashwinspanicker@gmail.com',
                    [email],
                    fail_silently=False,
                )   
                form.save()
                messages.success(request,"New Email Updated and Confirmation has sent")
                
                
               
        else:
            messages.success(request,"Incorrect Password")
                
    return render(request,"t_p_email.html",{'form':form,'cr':cr})


def t_m_list(request):
    idno=request.session['tidno']
    pswd=request.session['tpswd']
    user_details=teachers.objects.get(id_no=idno,password1=pswd)
    cr=user_details
    mr = s1.objects.all()
    print("t_m_list")
    return render(request,"t_updatemark.html",{'mr':mr,'cr':cr})
    

def t_m_update(request,pk):
    idno=request.session['tidno']
    pswd=request.session['tpswd']
    print(idno)
    user_details=teachers.objects.get(id_no=idno,password1=pswd)
    pr=user_details
    sub=request.session['sub']
    print(sub)
    print("t_m_update")
    if sub=="Physics":
        cr = s1.objects.get(id=pk)
        form = m_p_form(instance= cr)
        if request.method=="POST":
            form = m_p_form(request.POST,instance=cr)
            if form.is_valid:
                form.save()
                msg="Physics mark updated for " + cr.firstname + " " + cr.lastname + ", Register number : " + cr.reg_no 
                messages.success(request,msg)
                return redirect(t_m_list)
    if sub=="Electronics":
        cr = s1.objects.get(id=pk)
        form = m_e_form(instance= cr)
        if request.method=="POST":
            form = m_e_form(request.POST,instance=cr)
            if form.is_valid:
                form.save()
                msg="Electronics mark updated for " + cr.firstname + " " + cr.lastname + ", Register number : " + cr.reg_no
                messages.success(request,msg)
                return redirect(t_m_list)
    if sub=="Chemistry":
        cr = s1.objects.get(id=pk)
        form = m_c_form(instance= cr)
        if request.method=="POST":
            form = m_c_form(request.POST,instance=cr)
            if form.is_valid:
                form.save()
                msg="Chemistry mark updated for " + cr.firstname + " " + cr.lastname + ", Register number : " + cr.reg_no
                messages.success(request,msg)
                return redirect(t_m_list)
    
    if sub=="Mathematics":
        cr = s1.objects.get(id=pk)
        form = m_m_form(instance= cr)
        if request.method=="POST":
            form = m_m_form(request.POST,instance=cr)
            if form.is_valid:
                form.save()
                msg="Mathematics mark updated for " + cr.firstname + " " + cr.lastname + ", Register number : " + cr.reg_no
                messages.success(request,msg)
                return redirect(t_m_list)
            
    if sub=="Graphics":
        cr = s1.objects.get(id=pk)
        form = m_g_form(instance= cr)
        if request.method=="POST":
            form = m_g_form(request.POST,instance=cr)
            if form.is_valid:
                form.save()
                msg="Graphics mark updated for " + cr.firstname + " " + cr.lastname + ", Register number : " + cr.reg_no
                messages.success(request,msg)
                return redirect(t_m_list)
            
    return render(request,"t_updatemarklist.html",{'form':form,'cr':pr})


def t_leave(request):
    idno=request.session['tidno']
    pswd=request.session['tpswd']
    user_details=teachers.objects.get(id_no=idno,password1=pswd)
    cr=user_details
    pr=leave.objects.all().order_by('-id').values()
    return render(request,"t_leave.html",{'pr':pr,'cr':cr})

def t_viewleave(request,pk):
    cr = leave.objects.get(id=pk)
    return render(request,"t_viewleave.html",{'cr':cr})

def t_work_view(request):
    wrk="assignment"
    request.session['wrk']=wrk
    idno=request.session['tidno']
    pswd=request.session['tpswd']
    user_details=teachers.objects.get(id_no=idno,password1=pswd)
    cr=user_details
    sub=user_details.subject
    print(sub)
    s1=notes.objects.filter(semester="S1",subject=sub,session="Assignment").order_by('-id').values()
    s2=notes.objects.filter(semester="S2",subject=sub,session="Assignment").order_by('-id').values()
    return render(request,"t_view_work.html",{'cr':cr,'s1':s1,'s2':s2})


def t_work_home(request):
    wrk="homework"
    request.session['wrk']=wrk
    idno=request.session['tidno']
    pswd=request.session['tpswd']
    user_details=teachers.objects.get(id_no=idno,password1=pswd)
    cr=user_details
    sub=user_details.subject
    s1=notes.objects.filter(semester="S1",subject=sub,session="Homework").order_by('-id').values()
    s2=notes.objects.filter(semester="S2",subject=sub,session="Homework").order_by('-id').values()
    return render(request,"t_work_home.html",{'cr':cr,'s1':s1,'s2':s2})


    

def t_w_status(request,pk):
    idno=request.session['tidno']
    pswd=request.session['tpswd']
    wk=request.session['wrk']
    print(wk)
    user_details=teachers.objects.get(id_no=idno,password1=pswd)
    cr=user_details
    
    st = notes.objects.get(id=pk)
    form = n_s_form(instance= st)
    if request.method=="POST":
        form = n_s_form(request.POST,instance=st)
        if form.is_valid:
            form.save()
            if wk=="assignment":
                request.session['opt']="as"
                return redirect(t_work_view)
    
            elif wk=="homework":
                request.session['opt']="hw"
                return redirect(t_work_home)
            
    
    return render(request,"t_update_status.html",{'form':form,'cr':cr})

def t_notice(request):
    today = date.today()
    d = today.strftime("%d-%b-%Y")
    now = datetime.now()
    t = now.strftime("%H:%M")
    if request.method=='POST':
        t1=request.POST.get('t1')
        d1=request.POST.get('d1')
        t2=request.POST.get('time')
        d2=request.POST.get('d2')
        sem=request.POST.get('sem')
        note=request.POST.get('notice')
        print(t2)
        notices(todaydate=d1,todaytime=t1,time=t2,lastdate=d2,session=sem,content=note).save()
        messages.success(request,"Notice added to notice board")

    
    return render(request,"t_notice.html",{'date':d,'time':t})

### prinicpal session ####

def p_login(request):
    return render(request,"p_login.html")

def p_check(request):

    if request.method == "POST":
        idno = request.POST.get('idno')
        password = request.POST.get('password')
        print(idno)
        print(password)
        cr = principal.objects.filter(id_no=idno, password1=password)
        if cr:
            user_details=principal.objects.get(id_no=idno,password1=password)
            cr=user_details
            idno=user_details.id_no
            pswd=user_details.password1
            f=user_details.firstname
            l=user_details.lastname
            name=f +" "+ l
            email=user_details.email
            request.session['idno']=idno
            request.session['pswd']=pswd
            

            send_mail(
                'Login', #subject
                'hi ' +name+ ', Your successfully login. ' + 'Time :' +t+ ", Date " + today,
                'ashwinspanicker@gmail.com',
                [email],
                fail_silently=False,
            )
            messages.success(request,"Welcome To ST thomas Engineering college")
            return redirect(p_log)
        

        else:
            messages.success(request,"Check ID and Password ")
            return render(request,'p_login.html')
    
    else:
        return render(request,'t_login.html')


def p_log(request):
    idno=request.session['idno']
    pswd=request.session['pswd']
    user_details=principal.objects.get(id_no=idno,password1=pswd)
    cr=user_details
    
    
    pswd=user_details.password1
    
    request.session['pswd']=pswd
    print(idno)
    print(pswd)
    return render(request,"p_log.html",{'cr':cr})

def p_logout(request):
    logout(request)
    messages.success(request,("You were Signed out"))
    return redirect(p_login)

def p_profile(request):
    idno=request.session['idno']
    pswd=request.session['pswd']
    user_details=principal.objects.get(id_no=idno,password1=pswd)
    
    cr=user_details
    profile=user_details
    pswd=profile.password1
    email=profile.email
    print(pswd)
    f=profile.firstname
    l=profile.lastname
    name=f + " " + l
    form = p_p_form(instance=cr)
    if request.method=="POST":
        old=request.POST.get("old")
        print(old)
        p1=request.POST.get("password1")
        p2=request.POST.get("password2")
        if old==pswd:
            if p1==p2:
                form = p_p_form(request.POST,instance=cr)
                if form.is_valid:
                    form.save()
                    send_mail(
                    'Password Changed', #subject
                    'hi '+name+ ', your password is updated and you were signed out please sign in again.' +
                    
                    ' kindly login and check password ',

                    'ashwinspanicker@gmail.com',
                    [email],
                    fail_silently=False,
                    )
                    messages.success(request,"Password updated Sign in again")
                    logout(request)
                    return redirect(p_login)
                    
                else:
                    messages.success(request,"incorrect Password")      
                    
    return render(request,"p_password.html",{'form':form,'cr':cr})

def p_profile2(request):
    idno=request.session['idno']
    pswd=request.session['pswd']
    user_details=principal.objects.get(id_no=idno,password1=pswd)
    
    cr=user_details
    profile=user_details
    pswd=profile.password1
    
    print(pswd)
    f=user_details.firstname
    l=user_details.lastname
    name=f +" "+ l
    
    form = p_p_e_form(instance=cr)
    if request.method=="POST":
        email=request.POST.get("email")
        old=request.POST.get("old")
        print(old)
        
        
        
        if pswd==old:
            form = p_p_e_form(request.POST,instance=cr)
            if form.is_valid:
                send_mail(
                    'Email Updated', #subject
                    'hi '+name+ ', your profile Email is updated' +
                        
                    ' kindly verify your new email :' + email,

                    'ashwinspanicker@gmail.com',
                    [email],
                    fail_silently=False,
                )
                form.save()
                messages.success(request,"New Email Updated and Confirmation has sent")
                
                
            else:
                messages.success(request,"Entered Passwords Mismatched")      
        else:
            messages.success(request,"Oops Incorrect old Password")
                
    return render(request,"p_p_email.html",{'form':form,'cr':cr})


def p_students(request):
    idno=request.session['idno']
    pswd=request.session['pswd']
    cr=principal.objects.get(id_no=idno,password1=pswd)
    return render(request,"p_search.html",{'cr':cr})

def p_search(request):
    if request.method=='POST':
        sea=request.POST.get('search')
        print(sea)
        cr=students.objects.filter(reg_no=sea)
        
        if cr:
            print("inside if")
            cr=students.objects.get(reg_no=sea)
            m1=s1.objects.filter(reg_no=sea,).order_by('-id').values()
            #m2=s1.objects.filter(reg_no=sea,).order_by('-id').values()
            ass=notes.objects.filter(reg_no=sea,session="Assignment").order_by('-id').values()
            hwk=notes.objects.filter(reg_no=sea,session="Homework").order_by('-id').values()
            lv=leave.objects.filter(reg_no=sea).order_by('-id').values()
            print(sea)
            return render(request,"p_students.html",{'m1':m1,'ass':ass,'hw':hwk,'lv':lv,'cr':cr})
        else:
            messages.success(request,"Register number not exist")
            return render(request,"p_search.html")

        
        
    return render(request,"p_students.html")
    
