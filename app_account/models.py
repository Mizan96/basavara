from django.db import models

class ContactModel(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.email} - {self.timestamp}'