from django.db import models
from django.contrib.auth.models import User

class Listing(models.Model):
    """Model to represent a travel listing."""
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    location = models.CharField(max_length=255)
    available = models.BooleanField(default=True)

class Booking(models.Model):
    """Model to represent a booking for a listing."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

class Review(models.Model):
    """Model to represent a review for a listing."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
