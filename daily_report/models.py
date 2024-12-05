from django.db import models


# Create your models here.

class sliders(models.Model):
    slider_title = models.CharField(max_length=200, blank=False, null=False)
    slider_description = models.CharField(max_length=1000, blank=False, null=False)
    slider_photo = models.ImageField(upload_to="uploads/sliders", default="uploads/sliders/sliders.jpg")

    def __str__(self):
        return self.slider_title


class main_trending_headline(models.Model):
    trending_photo = models.ImageField(upload_to='uploads/main_trending', default='uploads/main_trending/main.jpg',
                                       blank=False, null=False)
    type_of_headline = models.CharField(max_length=200, null=False, blank=False)
    date = models.DateField(blank=False, null=False)
    trending_title = models.CharField(max_length=200, null=False, blank=False, default='')
    brief_description = models.TextField(blank=False, null=False)
    trending_description = models.TextField(default="", blank=False, null=False)
    related_image_1 = models.ImageField(upload_to='uploads/main_trending', default='uploads/main_trending/main.jpg',
                                        blank=True, null=True)
    related_image_2 = models.ImageField(upload_to='uploads/main_trending', default='uploads/main_trending/main.jpg',
                                        blank=True, null=True)
    related_image_3 = models.ImageField(upload_to='uploads/main_trending', default='uploads/main_trending/main.jpg',
                                        blank=True, null=True)
    writter_photo = models.ImageField(upload_to='uploads/writters', default='uploads/writters/writter.jpg', blank=False,
                                      null=False)
    writter_name = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.writter_name


class comment(models.Model):
    comm = models.TextField(null=False, blank=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField()
    phone = models.CharField(max_length=13, null=False, blank=False)

    def __str__(self):
        return self.full_name


class sub_trending_col_1(models.Model):
    trending_photo = models.ImageField(upload_to="uploads/sub trending col 1",
                                       default='uploads/sub trending col 1/sub.jpg')
    trending_choice = [
        ('Food', 'Food'),
        ('Sport', 'Sport'),
        ('Design', 'Design'),
        ('Business', 'Business'),
        ('Tech', 'Tech'),
        ('Travel', 'Travel')
    ]
    trending_type = models.CharField(max_length=30, null=False, blank=False, choices=trending_choice)
    date = models.DateField()
    title = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        return self.title


class sub_trending_col_2(models.Model):
    trending_photo = models.ImageField(upload_to="uploads/sub trending col 2",
                                       default='uploads/sub trending col 2/sub.jpg')
    trending_choice = [
        ('Food', 'Food'),
        ('Sport', 'Sport'),
        ('Design', 'Design'),
        ('Business', 'Business'),
        ('Tech', 'Tech'),
        ('Travel', 'Travel')
    ]
    trending_type = models.CharField(max_length=30, null=False, blank=False, choices=trending_choice)
    date = models.DateField()
    title = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        return self.title


class sub_trending_col_3(models.Model):
    trending_title = models.CharField(max_length=300, null=False, blank=False)
    writter = models.ImageField(upload_to='uploads/writters', default='uploads/writters/writter.jpg')

    def __str__(self):
        return self.trending_title
