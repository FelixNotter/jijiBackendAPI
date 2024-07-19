from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=450)

    def __str__(self):
        return self.name
    

class region(models.Model):
    name = models.CharField(max_length=450)

    def __str__(self):
        return self.name
    

class product(models.Model):
    name = models.CharField(max_length=450)
    description = models.TextField()
    price = models.FloatField()
    stock_quantity = models.IntegerField()
    category_id = models.ForeignKey(category, on_delete=models.CASCADE)
    region_id = models.ForeignKey(region, on_delete=models.CASCADE)
    product_url = models.CharField(null=True,blank=True,max_length=45000)
    
    
    def __str__(self):
        return self.name
    
class cart(models.Model):
    product_id = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True,blank=True)

    