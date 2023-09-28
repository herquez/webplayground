from django.contrib.auth.forms  import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserCreationEmail(UserCreationForm):
    email = forms.EmailField(
        required=True, 
        help_text='Requerido. 254 carácteres como máximo. Se enviará corréo de validación.'
    )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Ya hay una cuenta registrada con este email.')
        return email
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={
                'class': 'form-control-file mt-3'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Biografía'
            }),
            'link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://www.github.com/herquez'
            }),
        }

class EmailForm(forms.ModelForm):
    email = forms.EmailField(
        required=True, 
        help_text='Requerido. 254 carácteres como máximo. Se enviará corréo de validación.'
    )

    class Meta:
        model=User
        fields=('email',)
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('Ya hay una cuenta registrada con este email.')
        return email