from django.contrib.auth.forms  import UserCreationForm
from django import forms
from django.contrib.auth.models import User

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