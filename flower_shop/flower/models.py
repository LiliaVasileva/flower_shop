from django.db import models

class FlowerItem(models.Model):
    FLOWER_ITEM_NAME_MAX_LENGHT=50
    FLOWER_CATEGORY_NAME_MAX_LENGHT = 100
    FUNERAL = 'Погребения'
    WEDDING = 'Сватба'
    OTHER = 'Други'
    TYPES = [(x, x) for x in (FUNERAL, WEDDING, OTHER)]

    item_name = models.CharField(
        max_length= FLOWER_ITEM_NAME_MAX_LENGHT,
    )
    item_picture = models.ImageField(
        blank=True,
        null=True
    )
    item_price = models.FloatField()
    item_discription = models.TextField()
    item_category = models.CharField(
        max_length=FLOWER_CATEGORY_NAME_MAX_LENGHT,
        choices= TYPES,
        blank=True,
        null=True,
    )

