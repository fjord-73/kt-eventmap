from django.db import models
import os
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Visit(models.Model):
    prefecture = models.CharField(max_length=4)
    place = models.CharField(max_length=50)
    startrip = models.DateField()
    endtrip = models.DateField()
    photo = models.ImageField(upload_to ='media/')
    middle = ImageSpecField(source='photo',
                        processors=[ResizeToFill(600, 400)],
                        format="JPEG",
                        options={'quality': 75}
                        )
    comment = models.CharField(max_length=200)
    def __str__(self):
        return str(self.prefecture)+str(self.place)+str(self.comment)
#600*400なので横画像対象と記載