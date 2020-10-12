from django.db import models

# Create your models here.
class PerformerDetailModel(models.Model):
    name = models.CharField(max_length=100, null=True)
    e_name = models.CharField(max_length=100, null=True)
    alias = models.CharField(max_length=200, null=True)
    sex = models.CharField(max_length=10, default='')
    bloodtype = models.CharField(max_length=5, null=True)
    height = models.CharField(max_length=10,null=True)
    address = models.CharField(max_length=500, null=True)
    birthday = models.CharField(max_length=50, null=True)
    constellation = models.CharField(max_length=500, null=True)
    location = models.CharField(max_length=200, null=True)
    ResidentialAddress = models.CharField(max_length=100, null=True)
    school = models.CharField(max_length=200, null=True)
    BrokerageAgency = models.CharField(max_length=200, null=True)
    fameyear = models.CharField(max_length=200, null=True)
    hobby = models.CharField(max_length=1000, null=True)
    Occupation = models.CharField(max_length=500, null=True)
    weight = models.CharField(max_length=500, null=True)
    image = models.CharField(max_length=1000, null=True)
    des = models.CharField(max_length=2000, null=True)
    class Meta:
        db_table = "performerdetailtable"
