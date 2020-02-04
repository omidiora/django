from django import forms
from .models import RegistraionData

class RegistrationForm(forms.Form):
   username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={
      'class':'form-control',
      'placeholder':'username',

   }))
   password=forms.CharField(max_length=100,widget=forms.PasswordInput(
      attrs={'class':'form-control',
      'placeholder':'password',
      }))
   email=forms.CharField(max_length=100,widget=forms.TextInput(attrs={
      'class':'form-control',
      'placeholder':'Email',

   }))
   phone=forms.CharField(max_length=100,widget=forms.NumberInput(attrs={
      'class':'form-control',
      'placeholder':'Phone'
   }))    

class RegistrationModal(forms.ModelForm):
   class Meta:
      model=RegistraionData 
      fields=[
         'username',
         'password',
          'email',
          'phone',
      ]
