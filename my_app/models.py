from django.db import models

#from django.db import models

class Product(models.Model):
    product_id = models.CharField(max_length=50, primary_key=True)
    choices = (
        ('AVAILABLE','Item ready to be purchased'),
        ('RESTOCKING','Item restocking in few days')
    )
    status = models.CharField(max_length=50,choices=choices,default="AVAILABLE")

class Location(models.Model):
    location_id = models.CharField(max_length=50, primary_key=True)
    choices = (
        ('AVAILABLE','Place Available'),
        ('NOT AVAILABLE','Filled')
    )
    status = models.CharField(max_length=50,choices=choices,default="AVAILABLE")

class ProductMovement(models.Model):
    movement_id = models.CharField(max_length=50, primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    from_location = models.ForeignKey(Location, null=True, blank=True, related_name='from_location_item', on_delete=models.CASCADE)
    to_location = models.ForeignKey(Location, null=True, blank=True, related_name='to_location_item', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField()



    
    