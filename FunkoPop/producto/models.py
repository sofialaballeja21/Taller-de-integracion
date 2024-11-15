from django.db import models

# Create your models here.
class Producto(models.Model):
    name = models.CharField(max_length=128)
    number = models.IntegerField()
    collection = models.CharField(max_length=128)
    edition = models.CharField(max_length=128)
#    price = models.IntegerField()
    is_backlight = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.number} - {self.name}'
