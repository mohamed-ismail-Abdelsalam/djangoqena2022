from django import forms
from .models import *
class RegsiterForm(forms.Form):
    username=forms.CharField(max_length=20,label='Name',required=False)
    password=forms.CharField(max_length=12)
    confirmpassword=forms.CharField(max_length=12,label='Confirm')
    email=forms.EmailField(max_length=50)
    username.widget.attrs['class']='form-control form-control-user'
    password.widget.attrs['class']='form-control form-control-user'
    confirmpassword.widget.attrs['class']='form-control form-control-user'
    email.widget.attrs['class']='form-control form-control-user'
    #levels=forms.ChoiceField(choices=[(1,'python'),(2,'linux')])

class RegsiterFormmodel(forms.ModelForm):
    class Meta:
        model=Myuser
        fields ='__all__'
        #exclude=['email']