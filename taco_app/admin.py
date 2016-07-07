from django.contrib import admin
from taco_app.models import Food, Drink, EmployeeProfile, Extra, CustomerOrder


admin.site.register(Food)
admin.site.register(Drink)
admin.site.register(EmployeeProfile)
admin.site.register(Extra)
admin.site.register(CustomerOrder)
