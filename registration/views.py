from django.forms.models import BaseModelForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from .forms import UserCreationEmail, ProfileForm, EmailForm
from .models import Profile

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
    
@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        profile, created =  Profile.objects.get_or_create(user=self.request.user)
        return profile
    
@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    def get_object(self):
        # Recupera la instancia que queremos editar
        return self.request.user
    
    def get_form(self, form_class: type[BaseModelForm] | None = ...) -> BaseModelForm:
        form = super(EmailUpdate, self).get_form()
        form.fields['email'].widget = forms.EmailInput(
            attrs={
                'class': 'form-control mt-3',
                'placeholder': 'Email',
            }
        )
        return form