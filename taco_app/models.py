from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Food(models.Model):
    tortilla = models.CharField(max_length=20)
    protein = models.CharField(max_length=20)
    dress = models.CharField(max_length=20)
    finish = models.CharField(max_length=20)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=5, decimal_places=2)


class Drink(models.Model):
    name = models.CharField(max_length=20)
    portion = models.CharField(max_length=5)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=5, decimal_places=2)


class Extra(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=5, decimal_places=2)


class EmployeeProfile(models.Model):
    worker = models.OneToOneField('auth.User')
    nickname = models.CharField(max_length=20, null=True, blank=True)
    role = models.CharField(max_length=20)
    preferred_language = models.CharField(max_length=20)


class CustomerOrder(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    food_item = models.ForeignKey(Food)
    drink_item = models.ForeignKey(Drink)
    extra_item = models.ForeignKey(Extra)
    notes = models.CharField(max_length=250, null=True, blank=True)


class OrderLine(models.Model):
    order = models.ForeignKey(CustomerOrder)
    food = models.ForeignKey(Food)
    drink = models.ForeignKey(Drink)
    extra = models.ForeignKey(Extra)
    notes = models.CharField(max_length=250, null=True, blank=True)
    quantity = models.IntegerField()


@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')

    if created:
        EmployeeProfile.objects.create(user=instance)
