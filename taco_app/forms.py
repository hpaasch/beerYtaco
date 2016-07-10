from django import forms

from taco_app.models import OrderDrink, EmployeeProfile


class EmployeeProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = EmployeeProfile
        fields = ['nickname', 'role', 'preferred_language']

# this isn't being used. it was to put a second form on a page. but both can't be submitted at once.
# class OrderDrinkForm(forms.ModelForm):
#
#     class Meta:
#         model = OrderDrink
#         fields = ['order_tag', 'drink', 'drink_quantity', 'notes', 'order_up']


# class OrderDrinkForm(forms.ModelForm):
#     class Meta:
#         model = OrderDrink
#         fields = ['order_tag', 'drink', 'drink_quantity', 'notes']
#         widgets = {'drink': forms.RadioSelect}
