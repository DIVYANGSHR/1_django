from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    STATE_CHOICES = [
        ('AP', 'Andhra Pradesh'),
        ('AR', 'Arunachal Pradesh'),
        ('AS', 'Assam'),
        ('BR', 'Bihar'),
        ('CT', 'Chhattisgarh'),
        ('GA', 'Goa'),
        ('GJ', 'Gujarat'),
        ('HR', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
        ('JH', 'Jharkhand'),
        ('KA', 'Karnataka'),
        ('KL', 'Kerala'),
        ('MP', 'Madhya Pradesh'),
        ('MH', 'Maharashtra'),
        ('MN', 'Manipur'),
        ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'),
        ('NL', 'Nagaland'),
        ('OR', 'Odisha'),
        ('PB', 'Punjab'),
        ('RJ', 'Rajasthan'),
        ('SK', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('TG', 'Telangana'),
        ('TR', 'Tripura'),
        ('UP', 'Uttar Pradesh'),
        ('UK', 'Uttarakhand'),
        ('WB', 'West Bengal'),
        ('AN', 'Andaman and Nicobar Islands'),
        ('CH', 'Chandigarh'),
        ('DN', 'Dadra and Nagar Haveli and Daman and Diu'),
        ('DL', 'Delhi'),
        ('JK', 'Jammu and Kashmir'),
        ('LA', 'Ladakh'),
        ('LD', 'Lakshadweep'),
        ('PY', 'Puducherry'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    pincode = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.city}"


class Cake(models.Model):
    FLAVOR_CHOICES = [
        ('DONUTS', 'Donuts'),
        ('ICE CREAM', 'Ice Cream'),
        ('CUP CAKE', 'Cup Cake'),
        ('DELICIOUS CAKE', 'Delicious Cake'),
        ('CHOCOLATE CAKE', 'Chocolate CAKE'),
        ('SLICE CAKE', 'Slice Cake'),
    ]

    name = models.CharField(max_length=100)
    flavor = models.CharField(max_length=100, choices=FLAVOR_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    stock_quantity = models.PositiveIntegerField(default=10)
    cake_image = models.ImageField(upload_to='cake_images')

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.cake.name} ({self.quantity})"


class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"Order {self.id} - {self.cake.name} ({self.status})"

