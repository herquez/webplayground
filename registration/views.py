from django.forms.models import BaseModelForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms
from .forms import UserCreationEmail

class SignUpView(CreateView):
    form_class = UserCreationEmail
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get_success_url(self) -> str:
        return super().get_success_url() + '?registered'
    
    def get_form(self, form_class: type[BaseModelForm] | None = ...) -> BaseModelForm:
        form = super(SignUpView, self).get_form()
        form.fields['username'].widget = forms.TextInput(
            attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Nombre de usuario',
            }
        )
        form.fields['email'].widget = forms.EmailInput(
            attrs={
                'class': 'form-control mb-2',
                'placeholder': 'usuario@correo.com',
            }
        )
        form.fields['password1'].widget = forms.PasswordInput(
            attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Contraseña',
            }
        )
        form.fields['password2'].widget = forms.PasswordInput(
            attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Repetir contraseña',
            }
        )
        return form