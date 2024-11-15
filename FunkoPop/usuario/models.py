from django.db import models

class Usuario(models.Model):
    email = models.EmailField(unique=True)  # Asegura que el email sea único
    name = models.CharField(max_length=128)  # Nombre del usuario
    surname = models.CharField(max_length=128)  # Apellido del usuario
    phone = models.CharField(max_length=15, blank=True, null=True)  # Teléfono (opcional)
    address = models.CharField(max_length=255, blank=True, null=True)  # Dirección (opcional)
    
    def __str__(self):
        # Devuelve una representación en cadena más clara del usuario
        return f'{self.name} {self.surname} - {self.email}'





