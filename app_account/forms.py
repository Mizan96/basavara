from django import forms

from app_account.models import ContactModel

from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):
    name =  forms.CharField(label='Name',widget=forms.TextInput(
                attrs={
                    'class' :'form-control'
                    }
                )
            )
    email =  forms.CharField(label='Email',widget=forms.EmailInput(
                attrs={
                    'class' :'form-control'
                    }
                )
            )
    subject =  forms.CharField(label='Subject',widget=forms.TextInput(
                attrs={
                    'class' :'form-control'
                    }
                )
            )
    message =  forms.CharField(label='Message',widget=forms.TextInput(
                attrs={
                    'class' :'form-control'
                    }
                )
            )
    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'subject', 'message']

class SignupForm(forms.ModelForm):
    first_name =  forms.CharField(label='First name',widget=forms.TextInput(
                attrs={
                    'class' :'form-control'
                    }
                )
            )
    last_name =  forms.CharField(label='Last name',widget=forms.TextInput(
                attrs={
                    'class' :'form-control'
                    }
                )
            )
    username =  forms.CharField(label='Username',widget=forms.TextInput(
                attrs={
                    'class' :'form-control'
                    }
                )
            )
    email =  forms.CharField(label='Email',widget=forms.EmailInput(
                attrs={
                    'class' :'form-control'
                    }
                )
            )
    password =  forms.CharField(label='Password',widget=forms.PasswordInput(
                attrs={
                    'class' :'form-control'
                    }
                )
            )
    confirm_password =  forms.CharField(label='Confirm Password',widget=forms.PasswordInput(
                attrs={
                    'class' :'form-control'
                    }
                )
            )
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password', 'confirm_password']
    
    def clean_confirm_password(self):
        if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
            print('Not Macthed')
            raise forms.ValidationError('Password not match')
        return self.cleaned_data['confirm_password']
    
    def clean_email(self):
        if  User.objects.filter(email=self.cleaned_data['email']).count() > 0:
            raise forms.ValidationError('Email already exists')
        return self.cleaned_data['email']



class LoginForm(forms.ModelForm):
    password = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(
                attrs={
                    'class' :'form-control'
                    }
                )
            )
    username = forms.CharField(label='Username',widget=forms.TextInput(
                attrs={
                    'class' :'form-control'
                    }
                )
            )
    class Meta:
        model = User
        fields = ['username', 'password']