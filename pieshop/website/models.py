from django.db import models

# Create your models here.
class Pie(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    desc = models.TextField()
    image = models.ImageField(upload_to="images/", height_field=None, width_field=None, max_length=None, default="images/base-pie.png")

    def __str__(self):
        return self.title

class Order(models.Model):
    pie = models.ForeignKey(Pie, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100)
    secondName = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postcode = models.CharField(max_length=100)
    deliverDate = models.DateTimeField()
    comments = models.TextField(blank=True, default='')

    def __str__(self):
        return f"{self.firstName}, {self.pie}, {self.deliverDate}"