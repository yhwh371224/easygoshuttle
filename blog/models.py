from django.db import models
from django.apps import AppConfig
from django.urls import reverse


class Inquiry(models.Model):
    name = models.CharField(max_length=100, blank=False)
    contact = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)

    flight_date = models.DateField(verbose_name='flight_date', blank=False)
    flight_number = models.CharField(max_length=100, blank=False)
    flight_time = models.CharField(max_length=30, blank=False)
    pickup_time = models.CharField(max_length=30, blank=True)

    direction = models.CharField(max_length=100, blank=False)
    suburb = models.CharField(max_length=100, blank=False)
    street = models.CharField(max_length=200, blank=False)

    no_of_passenger = models.CharField(max_length=30, blank=False)
    no_of_baggage = models.CharField(max_length=200, blank=True)
    message = models.TextField(blank=True)
    notice = models.TextField(blank=True)
    
    price = models.CharField(max_length=30, blank=True)    
    paid = models.CharField(max_length=30, blank=True)

    is_confirmed = models.BooleanField(default=False, blank=True)    
    reConfirmed = models.BooleanField(default=False, blank=True)
    
    cancelled = models.BooleanField(default=False, blank=True)
    
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
    
    def get_absolute_url(self):
        return '/blog/inquiry{}/'.format(self.pk)

        
class Post(models.Model):
    name = models.CharField(max_length=100, blank=False)
    contact = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)

    flight_date = models.DateField(verbose_name='flight_date', blank=False)
    flight_number = models.CharField(max_length=100, blank=False)
    flight_time = models.CharField(max_length=30, blank=False)
    pickup_time = models.CharField(max_length=30, blank=True)

    direction = models.CharField(max_length=100, blank=False)
    suburb = models.CharField(max_length=100, blank=False)
    street = models.CharField(max_length=200, blank=False)

    no_of_passenger = models.CharField(max_length=30, blank=False)
    no_of_baggage = models.CharField(max_length=200, blank=True)
    message = models.TextField(blank=True)
    notice = models.TextField(blank=True)    

    price = models.CharField(max_length=30, blank=True)
    paid = models.CharField(max_length=30, blank=True)

    is_confirmed = models.BooleanField(default=False, blank=True)    
    reConfirmed = models.BooleanField(default=False, blank=True)
    
    cancelled = models.BooleanField(default=False, blank=True)
    
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        return '/blog/{}/'.format(self.pk)


class BlogAppConfig(AppConfig):
    name = 'blog'

    def ready(self):
        from . import signals
