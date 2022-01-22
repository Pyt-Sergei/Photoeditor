from django.db import models

import datetime


class ImageModel(models.Model):
    image = models.ImageField('image', upload_to='images/')
    date = models.DateTimeField('date', default=datetime.datetime.now)

    class Meta:
        ordering = ['-date']
