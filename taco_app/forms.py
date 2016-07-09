from django import forms

from taco_app.models import OrderDrink


class OrderDrinkForm(forms.ModelForm):

    class Meta:
        model = OrderDrink
        fields = ['order_tag', 'drink', 'drink_quantity', 'notes', 'order_up']
