from django.contrib import admin
from taco_app.models import Food, Drink, EmployeeProfile, Extra, Customer, OrderFood, OrderDrink


admin.site.register(Food)
admin.site.register(Drink)
admin.site.register(EmployeeProfile)
admin.site.register(Extra)
admin.site.register(Customer)
admin.site.register(OrderFood)
admin.site.register(OrderDrink)
