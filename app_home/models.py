from django.db import models
from django.contrib.auth.models import User


class CityModel(models.Model):
    city = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city



class AreaModel(models.Model):
    area = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.area


class ToLetModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # city = models.CharField(max_length=120)
    # area = models.CharField(max_length=120)
    city = models.ForeignKey(CityModel, on_delete=models.SET_NULL, null=True)
    area = models.ForeignKey(AreaModel, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    mobile = models.CharField(max_length=15)
    address = models.TextField(null=True, blank=True)
    description = models.TextField()
    image1 = models.ImageField(upload_to='tolet', null=True, blank=True)
    image2 = models.ImageField(upload_to='tolet', null=True, blank=True)
    image3 = models.ImageField(upload_to='tolet', null=True, blank=True)
    open = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.city} - {self.area} - {self.timestamp}'

    class Meta:
        ordering = ['-timestamp']


class ToletCommentModel(models.Model):
    tolet = models.ForeignKey(ToLetModel, on_delete=models.CASCADE)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.tolet} - {self.comment}'
    
    class Meta:
        ordering = ['-timestamp']

class HomeOwnerMessageModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.message}'
    
    class Meta:
        ordering = ['-timestamp']
