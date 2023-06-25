from django.db import models

# Create your models here.
class Fruit(models.Model):
    # 품명
    f_name = models.CharField(max_length=10)
    # 수량
    value = models.BigIntegerField()