from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Food(models.Model):
    name = models.CharField(max_length=20, default='add taco')
    tortilla = models.CharField(max_length=20)
    protein = models.CharField(max_length=20)
    dress = models.CharField(max_length=20)
    finish = models.CharField(max_length=20)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=20, default='add drink')
    portion = models.CharField(max_length=10)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Extra(models.Model):
    name = models.CharField(max_length=20, default='add extra')
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class EmployeeProfile(models.Model):
    worker = models.OneToOneField('auth.User')
    nickname = models.CharField(max_length=20, null=True, blank=True)
    role = models.CharField(max_length=20)
    preferred_language = models.CharField(max_length=20, default='English')

    def __str__(self):
        return self.nickname


class Customer(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    tag_number = models.SlugField(null=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return (self.tag_number)


class OrderFood(models.Model):
    order_tag = models.ForeignKey(Customer)
    food = models.ForeignKey(Food, null=True)
    food_quantity = models.IntegerField(null=True)
    extra = models.ForeignKey(Extra, null=True)
    extra_quantity = models.IntegerField(null=True)
    notes = models.CharField(max_length=250, null=True, blank=True)
    order_up = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.order_tag)

    class Meta:
        ordering = ['created']


class OrderDrink(models.Model):
    order_tag = models.ForeignKey(Customer)
    drink = models.ForeignKey(Drink, null=True)
    drink_quantity = models.IntegerField(null=True)
    notes = models.CharField(max_length=250, null=True, blank=True)
    order_up = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.order_tag)

    class Meta:
        ordering = ['-created', 'order_tag']


@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')

    if created:
        EmployeeProfile.objects.create(user=instance)
