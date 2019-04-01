from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=40)
    website = models.URLField()


class ShoeType(models.Model):
    style = models.CharField(max_length=40)


class ShoeColor(models.Model):
    color_name = models.CharField(max_length=20)


class Shoe(models.Model):
    size = models.IntegerField()
    brand_name = models.CharField(max_length=20)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=20)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=20)
