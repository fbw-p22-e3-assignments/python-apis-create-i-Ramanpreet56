from django.db import models

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=150)
    #product_id = models.BigAutoField(primary_key=True)
    product_category = models.CharField(max_length=150)
    product_description= models.TextField(max_length=400)
    product_image_url = models.URLField()
    product_price= models.PositiveIntegerField()

    def __str__(self) ->str:
        return self.product_name