from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Member(models.Model):
  firstname = models.CharField(max_length=255, null=False, verbose_name="First Name")
  lastname = models.CharField(max_length=255, null=False, verbose_name="Last Name")
  ddd_phone = models.CharField(null=True, max_length=2, validators=[MinLengthValidator(2)], verbose_name="DDD")
  phone = models.CharField(max_length=15, null=True, verbose_name="Phone Number")
  joined_date = models.DateField(null=True, verbose_name="Member since")

  def __str__(self):
    return f"{self.firstname} {self.lastname}"