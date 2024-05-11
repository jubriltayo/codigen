from django.db import models
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File

# Create your models here.
class Product(models.Model):
    barcode_id = models.CharField(max_length=5)
    name = models.CharField(max_length=200)
    barcode = models.ImageField(upload_to='images/', blank=True)
    country_id = models.CharField(max_length=1)
    manufacturer_id = models.CharField(max_length=6)
    number_id = models.CharField(max_length=5)

    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
        EAN = barcode.get_barcode_class('ean13')
        ean = EAN(f'{self.country_id}{self.manufacturer_id}{self.number_id}', writer=ImageWriter())
        buffer = BytesIO()
        ean.write(buffer)
        self.barcode.save(f'{self.barcode_id}{self.country_id}{self.manufacturer_id}{self.number_id}.png', File(buffer), save=False)
        return super().save(*args, **kwargs)
    