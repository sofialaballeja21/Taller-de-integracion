from django import forms

from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from usuario.models import Usuario
from datetime import datetime

class UsuarioForm(forms.ModelForm):
    
    phone = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = Usuario
        fields = [
            'email',
            'name',
            'surname',
            'address',
            'phone',
        ]

    # Validaciones 
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) < 10:
            raise forms.ValidationError('El número de teléfono debe tener al menos 10 dígitos.')
        return phone

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email

