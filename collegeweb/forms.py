from django import forms
from django import views
from .models import students,teachers,principal,s1,notes
from django.forms.widgets import RadioSelect



class s_form(forms.ModelForm):
    
    
    password1=forms.CharField(widget=forms.TextInput(attrs={
            "class":"input",
            "type":"password",
            "name":"password1",
            
        }),label="Password")
    
    password2=forms.CharField(widget=forms.TextInput(attrs={
            "class":"input",
            "type":"password",
            "name":"password2",
            
        }),label="Confirm Password")
    
    email=forms.CharField(widget=forms.TextInput(attrs={
            "class":"input",
            "type":"email",
            "name":"email",
            "class":"form-control",
            
        }),label="Email")
    
    reg_no=forms.CharField(widget=forms.TextInput(attrs={
            "class":"input",
            "type":"number",
            
            "class":"form-control",
            
        }),label="Register Number")
    
    
    gender = forms.ChoiceField(required=True, widget=forms.RadioSelect(
    attrs={'class': 'Radio'}), choices=(('male','Male'),('female','Female'),))

    
    
    class Meta:
        model = students

        fields=('firstname','lastname','email','place','guardian_phone','reg_no','department','semaster','password1','password2','gender','image')

        widgets={
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.RadioSelect(attrs={'class':'form-control'}),
            'reg_no':forms.TextInput(attrs={'class':'form-control'}),
            'place':forms.TextInput(attrs={'class':'form-control'}),
            
            'department':forms.TextInput(attrs={'class':'form-control'}),
            'semester':forms.TextInput(attrs={'class':'form-control'}),
            
            'password1':forms.PasswordInput(attrs={'class':'form-control'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control'}),
            
            'image':forms.FileInput(attrs={'class':'form-control'}),
          

        }

class t_form(forms.ModelForm):

    password1=forms.CharField(widget=forms.TextInput(attrs={
            "class":"input",
            "type":"password",
            "name":"password1",
            
        }),label="Password")
    
    password2=forms.CharField(widget=forms.TextInput(attrs={
            "class":"input",
            "type":"password",
            "name":"password2",
            
        }),label="Confirm Password")
    
    SUBJECT_CHOICES= [
    ('Physics', 'Physics'),
    ('Chemistry', 'Chemistry'),
    ('Mathematics', 'Mathematics'),
    ('Electronics', 'Electronics'),
    ('Graphics', 'Graphics'),
    ]
    
    subject= forms.CharField( widget=forms.Select(choices=SUBJECT_CHOICES,attrs={'class':'form-control',}))
    gender = forms.ChoiceField(required=True, widget=forms.RadioSelect(
    attrs={'class': 'Radio'}), choices=(('male','Male'),('female','Female'),))

    class Meta:
        model = teachers

        fields=('firstname','lastname','email','contact_no','id_no','department','subject','password1','password2','gender','image')

        widgets={
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.RadioSelect(attrs={'class':'form-control'}),
            'contact_no':forms.TextInput(attrs={'class':'form-control'}),
            'id_no':forms.TextInput(attrs={'class':'form-control'}),
            'subject':forms.TextInput(attrs={'class':'form-control'}),
            'department':forms.TextInput(attrs={'class':'form-control'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
        }

class p_form(forms.ModelForm):
    password1=forms.CharField(widget=forms.TextInput(attrs={
            "class":"form-control",
            "type":"password",
            "name":"password1",
            
        }),label="Password")
    
    password2=forms.CharField(widget=forms.TextInput(attrs={
            "class":"form-control",
            "type":"password",
            "name":"password2",
            
        }),label="Confirm Password")
    
    gender = forms.ChoiceField(required=True, widget=forms.RadioSelect(
    attrs={'class': 'Radio'}), choices=(('male','Male'),('female','Female'),))

    class Meta:
        model = principal

        fields=('firstname','lastname','email','contact_no','id_no','password1','password2','gender','image')

        widgets={
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.RadioSelect(attrs={'class':'form-control'}),
            'contact_no':forms.TextInput(attrs={'class':'form-control'}),
            'id_no':forms.TextInput(attrs={'class':'form-control','label':'ID'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
        }

class t_p_form(forms.ModelForm):
    old=forms.CharField(widget=forms.TextInput(attrs={
            "class":"form-control",
            "type":"password",
            "name":"old",
            
        }),label="Old Password")
    
    
    password1=forms.CharField(widget=forms.TextInput(attrs={
            "class":"form-control",
            "type":"password",
            "name":"password1",
            "onpaste":"return false",
            "onCopy":"return false",
            "onCut":"return false",
            
        }),label="New Password",)
    
    password2=forms.CharField(widget=forms.TextInput(attrs={
            "class":"form-control",
            "type":"password",
            "name":"password2",
            "onpaste":"return false",
            "onCopy":"return false",
            "onCut":"return false",
            
            
        }),label="Confirm Password")
    
    
    class Meta:
        model = teachers

        fields=('password1','password2',)

        widgets={
            
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password1':forms.TextInput(attrs={'class':'form-control'}),
            
        }

class t_p_e_form(forms.ModelForm):
    old=forms.CharField(widget=forms.TextInput(attrs={
            "class":"form-control",
            "type":"password",
            "name":"old",

            
        }),label="Profile Password")
    
    
    
    
    
    class Meta:
        model = teachers

        fields=('email',)

        widgets={
            
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password1':forms.TextInput(attrs={'class':'form-control'}),
            
        }





class m_p_form(forms.ModelForm):
   
    RESULT_CHOICES= [
    ('PASSED', 'PASSED'),
    ('FAILED', 'FAILED'),
    ('PENDING', 'PENDING'),
    ]

    p_res= forms.CharField( widget=forms.Select(choices=RESULT_CHOICES,attrs={'class':'form-control',}),label="Result")

    class Meta:
        model=s1

        fields=('physics','p_res')

        widgets={
            'physics':forms.TextInput(attrs={'class':'form-control'}),
            
        }

class m_e_form(forms.ModelForm):

    RESULT_CHOICES= [
    ('PASSED', 'PASSED'),
    ('FAILED', 'FAILED'),
    ('PENDING', 'PENDING'),
    ]

    e_res= forms.CharField( widget=forms.Select(choices=RESULT_CHOICES,attrs={'class':'form-control',}),label="Result")

    class Meta:
        model=s1

        fields=('electronics','e_res')

        widgets={
            'electronics':forms.TextInput(attrs={'class':'form-control'}),
        }

class m_c_form(forms.ModelForm):

    RESULT_CHOICES= [
    ('PASSED', 'PASSED'),
    ('FAILED', 'FAILED'),
    ('PENDING', 'PENDING'),
    ]

    c_res= forms.CharField( widget=forms.Select(choices=RESULT_CHOICES,attrs={'class':'form-control',}),label="Result")

    class Meta:
        model=s1

        fields=('chemistry','c_res')

        widgets={
            'chemistry':forms.TextInput(attrs={'class':'form-control'}),
        }

class m_m_form(forms.ModelForm):
   
    RESULT_CHOICES= [
    ('PASSED', 'PASSED'),
    ('FAILED', 'FAILED'),
    ('PENDING', 'PENDING'),
    ]

    m_res= forms.CharField( widget=forms.Select(choices=RESULT_CHOICES,attrs={'class':'form-control',}),label="Result")
            
    class Meta:
        model=s1

        fields=('mathematics','m_res')

        widgets={
            'mathematics':forms.TextInput(attrs={'class':'form-control'}),
        }

class m_g_form(forms.ModelForm):

    RESULT_CHOICES= [
    ('PASSED', 'PASSED'),
    ('FAILED', 'FAILED'),
    ('PENDING', 'PENDING'),
    ]

    g_res= forms.CharField( widget=forms.Select(choices=RESULT_CHOICES,attrs={'class':'form-control',}),label="Result") 

    class Meta:
        model=s1

        fields=('graphics','g_res')

        widgets={
            'graphics':forms.TextInput(attrs={'class':'form-control'}),
        }






class n_s_form(forms.ModelForm):

    STATUS_CHOICES= [
    ('On time', 'On time'),
    ('Earlier', 'Earlier'),
    ('Delayed', 'Delayed'),
    ]

    status= forms.CharField( widget=forms.Select(choices=STATUS_CHOICES,attrs={'class':'form-control',}),label="Status")

    class Meta:
        model=notes

        fields=('status',)

        widgets={
            'status':forms.TextInput(attrs={'class':'form-control'}),
        }

class s_p_p_form(forms.ModelForm):
    old=forms.CharField(widget=forms.TextInput(attrs={
            "class":"form-control",
            "type":"password",
            "name":"old",
            "onpaste":"return false",
            "onCopy":"return false",
            "onCut":"return false",
            
        }),label="Old Password")
    
    
    password1=forms.CharField(widget=forms.TextInput(attrs={
            "class":"form-control",
            "type":"password",
            "name":"password1",
            "onpaste":"return false",
            "onCopy":"return false",
            "onCut":"return false",
            
            
        }),label="New Password",)
    
    password2=forms.CharField(widget=forms.TextInput(attrs={
            "class":"form-control",
            "type":"password",
            "name":"password2",
            "onpaste":"return false",
            "onCopy":"return false",
            "onCut":"return false",
            
        }),label="Confirm Password")
    
    
    class Meta:
        model = students

        fields=('password1','password2',)

        widgets={
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password1':forms.TextInput(attrs={'class':'form-control'}),
            
        }

class s_p_e_form(forms.ModelForm):
    old=forms.CharField(widget=forms.TextInput(attrs={
            "class":"form-control",
            "type":"password",
            "name":"old",
            
        }),label="Profile Password")
    
    
    
    class Meta:
        model = students

        fields=('email',)

        widgets={
            'email':forms.TextInput(attrs={'class':'form-control'}),
            
            
        }

class s_upnotes(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control",
        "type":"text",
        "readonly":"readonly",
    }))

    department=forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control",
        "type":"text",
        "readonly":"readonly",
    }))

    semester=forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control",
        "type":"text",
        "readonly":"readonly",
    }))

    upload_date=forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control",
        "type":"text",
        "readonly":"readonly",
    }))

    SUBJECT_CHOICES= [
    ('Physics', 'Physics'),
    ('Chemistry', 'Chemistry'),
    ('Mathematics', 'Mathematics'),
    ('Electronics', 'Electronics'),
    ('Graphics', 'Graphics'),

    ]
    FILE_CHOICES= [
    ('PDF', 'PDF'),
    ('DOC', 'DOC'),
    ('TXT', 'TEXT'),
    ('PPT', 'PPT'),
    ('IMG', 'IMAGE'),
    ]

    SESSION_CHOICES= [
    ('Homework', 'Homework'),
    ('Assignment', 'Assignment'),
    ]



    subject= forms.CharField( widget=forms.Select(choices=SUBJECT_CHOICES,attrs={'class':'form-control','name':'sub'}))

    filetype= forms.CharField( widget=forms.Select(choices=FILE_CHOICES,attrs={'class':'form-control',}))

    session= forms.CharField( widget=forms.Select(choices=SESSION_CHOICES,attrs={'class':'form-control',}),label="Category")

    class Meta:
        model=notes
        fields=('name','department','semester','upload_date','subject','session','filetype','file',)

        widgets={
            'file':forms.FileInput(attrs={'class':'form-control'}),
            
            
        }
        

class p_p_form(forms.ModelForm):
    old=forms.CharField(widget=forms.TextInput(attrs={
            "class":"form-control",
            "type":"password",
            "name":"old",
            "onpaste":"return false",
            "onCopy":"return false",
            "onCut":"return false",
            
        }),label="Old Password")
    
    
    password1=forms.CharField(widget=forms.TextInput(attrs={
            "class":"form-control",
            "type":"password",
            "name":"password1",
            "onpaste":"return false",
            "onCopy":"return false",
            "onCut":"return false",
            
        }),label="New Password",)
    
    password2=forms.CharField(widget=forms.TextInput(attrs={
            "class":"form-control",
            "type":"password",
            "name":"password2",
            "onpaste":"return false",
            "onCopy":"return false",
            "onCut":"return false",
            
        }),label="Confirm Password")
    
    
    class Meta:
        model = principal

        fields=('password1','password2',)

        widgets={
            
            
            
            
        }


class p_p_e_form(forms.ModelForm):
    old=forms.CharField(widget=forms.TextInput(attrs={
            "class":"form-control",
            "type":"password",
            "name":"old",
            
        }),label="Profile Password")
    
    
    
    
    
    
    
    class Meta:
        model = principal

        fields=('email',)

        widgets={
            
            'email':forms.TextInput(attrs={'class':'form-control'}),
            
            
        }