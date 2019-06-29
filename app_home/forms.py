from django.contrib.auth.models import User
from django import forms
from app_home.models import ToLetModel, CityModel, AreaModel


class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(label='First name', widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    )
    )
    last_name = forms.CharField(label='Last name', widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    )
    )
    email = forms.CharField(label='Email', widget=forms.EmailInput(
        attrs={
            'class': 'form-control'
        }
    )
    )

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
        ]

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).count() > 1:
            raise forms.ValidationError('Email already exists')
        return self.cleaned_data['email']


class PostToLetForm(forms.ModelForm):
    # city = forms.CharField(label='City', widget=forms.TextInput(
    #     attrs={
    #         'class': 'form-control',
    #         'placeholder': 'শহর'
    #     }
    # )
    # )
    # area = forms.CharField(label='Area', widget=forms.TextInput(
    #     attrs={
    #         'class': 'form-control',
    #         'placeholder': 'এলাকা'
    #     }
    # )
    # )
    price = forms.CharField(label='Price', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'ভাড়া'
        }
    )
    )
    mobile = forms.CharField(label='Mobile', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'মোবাইল নাম্বার'
        }
    )
    )
    description = forms.CharField(label='Description', widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'বিবরণ'
        }
    )
    )
    address = forms.CharField(label='Address', widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'ঠিকানা'
        }
    )
    )
    # image1 = forms.FileField(label='Image1', widget=forms.ClearableFileInput(
    #     attrs={
    #        'class': 'custom-file-input',
    #
    #     }
    # ))
    # image2 = forms.FileField(label='Image2', widget=forms.ClearableFileInput(
    #     attrs={
    #        'class': 'custom-file-input'
    #     }
    # ))
    # image3 = forms.FileField(label='Image3', widget=forms.ClearableFileInput(
    #     attrs={
    #        'class': 'custom-file-input'
    #     }
    # ))

    class Meta:
        model = ToLetModel
        fields = [
            'city',
            'area',
            'price',
            'mobile',
            'address',
            'description',
            'image1',
            'image2',
            'image3',
            'open'
        ]
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['area'].queryset = AreaModel.objects.none()
