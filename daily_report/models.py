from django.db import models


# Create your models here.

class sliders(models.Model):
    slider_title = models.CharField(max_length=20, blank=False, null=False)
    slider_description = models.CharField(max_length=50, blank=False, null=False)
    slider_photo = models.ImageField(upload_to="uploads/sliders", default="uploads/sliders/sliders.jpg")

    def __str__(self):
        return self.slider_title

