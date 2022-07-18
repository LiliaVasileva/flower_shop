from django.db import models

class FlowerItem(models.Model):
    FLOWER_ITEM_NAME_MAX_LENGHT=50
    item_name = models.CharField(
        max_length= FLOWER_ITEM_NAME_MAX_LENGHT,
    )
    item_picture = models.ImageField(
        blank=True,
        null=True
    )
    item_price = models.FloatField()
    item_discription = models.TextField()

