from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.
class Youtuber(models.Model):
    crew_choices = (
        ('solo', 'solo'),
        ('small', 'small'),
        ('large', 'large'),
    )


    camera_choices = (
        ('cannon', 'cannon'),
        ('nikon', 'nikon'),
        ('sony', 'sony'),
        ('red', 'red'),
        ('fuji', 'fuji'),
        ('panasonic', 'panasonic'),
        ('other', 'other'),
    )



    catagory_choices = (
        ('code', 'code'),
        ('mobile', 'mobile'),
        ('vlog', 'vlog'),
        ('comedy', 'comedy'),
        ('gaming', 'gaming'),
        ('film_making', 'film_making'),
        ('cooking', 'cooking'),
    )



    name = models.CharField(max_length=225)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='media/ytubers/%Y/%m/')
    video_url = models.CharField(max_length=225)
    discription = RichTextField()
    city = models.CharField(max_length=225)
    age = models.IntegerField()
    height = models.IntegerField()
    crew = models.CharField(choices=crew_choices,max_length=225)
    cemera_type = models.CharField(choices=camera_choices, max_length=225)
    category = models.CharField(choices=catagory_choices,max_length=225)
    is_featured = models.BooleanField(max_length=225)
    subs_count = models.CharField(max_length=225)
    crated_data = models.DateTimeField(default=datetime.now, blank=True)