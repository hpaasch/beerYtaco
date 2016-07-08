from django.contrib import admin
from taco_app.models import Food, Drink, EmployeeProfile, Extra, Customer, OrderFood, OrderDrink


class OrderFoodAdmin(admin.ModelAdmin):
    list_display = ['order_tag', 'order_up', 'created']
    search_fields = ['order_tag']

admin.site.register(Food)
admin.site.register(Drink)
admin.site.register(EmployeeProfile)
admin.site.register(Extra)
admin.site.register(Customer)
admin.site.register(OrderFood, OrderFoodAdmin)
admin.site.register(OrderDrink)
