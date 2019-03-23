from django.db import models
from datetime import datetime

class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(null=True)
    contact_date = models.DateTimeField(default=datetime.now, null=True)
    user_id = models.IntegerField(null=True)
    def __str__(self):
        return self.name


