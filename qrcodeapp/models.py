from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

# Create your models here.
class Link(models.Model):
    name = models.CharField(max_length=100)
    qrcode = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        qr_image = qrcode.make(self.name)
        qr_offset = Image.new('RGB', (310, 310), 'white')
        qr_offset.paste(qr_image)
        files_name = f'{self.name}-{self.id}qr.png'
        stream = BytesIO()
        qr_offset.save(stream, 'PNG')
        self.qrcode.save(files_name, File(stream), save=False)
        qr_offset.close()
        return super().save(*args, **kwargs)
