from django import forms
from myuser.models import *
class Register(forms.Form):
    username=forms.CharField(label='User Name',max_length=20)
    password=forms.CharField(label='Password',max_length=12)
    confirmpassword=forms.CharField(label='Confirm Password',max_length=12)
    email=forms.EmailField(label='asd',max_length=50)
    email.widget.attrs['class']='form-control form-control-user'

class Register2(forms.ModelForm):
    class Meta:
        model=Myuser
        fields='__all__'