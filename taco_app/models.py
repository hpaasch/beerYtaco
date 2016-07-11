from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

SERVER = 'Server'
BARTENDER = 'Bartender'
COOK = 'Cook'
MANAGER = 'Manager'
ENGLISH = 'English'
SPANISH = 'Spanish'


class Food(models.Model):
    name = models.CharField(max_length=20, default='add taco')
    tortilla = models.CharField(max_length=20)
    protein = models.CharField(max_length=20)
    dress = models.CharField(max_length=60)
    finish = models.CharField(max_length=60)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=20, default='add drink')
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
    ROLE_CHOICES = (
        (SERVER, 'Server'),
        (BARTENDER, 'Bartender'),
        (COOK, 'Cook'),
        (MANAGER, 'Manager')
        )
    worker = models.OneToOneField('auth.User')
    nickname = models.CharField(max_length=20, null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=SERVER)
    LANGUAGE_CHOICES = (
        (ENGLISH, 'English'),
        (SPANISH, 'Spanish'),
        )
    preferred_language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES, default=ENGLISH)

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
    placed_by = models.ForeignKey(User, null=True)
    food = models.ForeignKey(Food, null=True, blank=True)
    food_quantity = models.PositiveIntegerField(null=True, default=0)
    extra = models.ForeignKey(Extra, null=True, blank=True)
    extra_quantity = models.PositiveIntegerField(null=True, default=0)
    notes = models.CharField(max_length=250, null=True, blank=True)
    order_up = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.order_tag)

    class Meta:
        ordering = ['created']


class OrderDrink(models.Model):
    order_tag = models.ForeignKey(Customer)
    placed_by = models.ForeignKey(User, null=True)
    drink = models.ForeignKey(Drink, null=True, blank=True)
    drink_quantity = models.PositiveIntegerField(null=True, blank=True)
    notes = models.CharField(max_length=250, null=True, blank=True)
    order_up = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.order_tag)

    class Meta:
        ordering = ['created']


@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')

    if created:
        EmployeeProfile.objects.create(worker=instance)
