from django.db import models
from real_estate.models import User

# Create your models here.
type_choices = (
    ("duplex", "duplex"),
    ("mansion", "mansion"),
    ("flat", "flat"),
    ("apartment", "apartment"),
    ("full_house", "house"),
)


class Property(models.Model):
    property_title = models.CharField(max_length=255)
    _type = models.CharField(max_length=30, choices=type_choices, default="full_house")
    price = models.DecimalField(max_digits=9, decimal_places=2)
    bedrooms = models.PositiveIntegerField()
    is_rental = models.BooleanField(default=False)
    is_sale = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="properties")


class Address(models.Model):
    country = models.CharField(max_length=70)
    city = models.CharField(max_length=70, null=True, blank=True)
    state = models.CharField(max_length=60)
    zipcode = models.CharField()
    street_add = models.CharField()
    property = models.OneToOneField(
        Property, on_delete=models.CASCADE, related_name="address"
    )


class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name="property_messages"
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")


class Property_image(models.Model):
    img = models.ImageField()
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name="images"
    )
