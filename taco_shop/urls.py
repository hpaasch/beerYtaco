
from django.conf.urls import url, include
from django.contrib import admin

from taco_app.views import CreateAccountView, AccountProfileView, EmployeeProfileUpdateView, CreateFoodView, CreateExtraView

from taco_app.views import IndexView, OrderFoodView, OrderDrinkView, ShowFoodOrder, UpdateFoodOrder, ShowDrinkOrder, UpdateDrinkOrder, PendingCustomers, ShowCustomerOrder

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^create_account/$', CreateAccountView.as_view(), name='create_account_view'),
    url(r'accounts/profile/$', AccountProfileView.as_view(), name='account_profile_view'),
    url(r'accounts/profile/update/$', EmployeeProfileUpdateView.as_view(), name='employee_profile_update_view'),
    url(r'food/$', OrderFoodView.as_view(), name='order_food_view'),
    url(r'food/create/$', CreateFoodView.as_view(), name='create_food_view'),
    url(r'food/create/extra$', CreateExtraView.as_view(), name='create_extra_view'),
    url(r'food/orders/$', ShowFoodOrder.as_view(), name='show_food_order_view'),
    url(r'food/orders/update/(?P<pk>\d+)/$', UpdateFoodOrder.as_view(), name='update_food_order_view'),
    url(r'drink/$', OrderDrinkView.as_view(), name='order_drink_view'),
    url(r'drink_orders/$', ShowDrinkOrder.as_view(), name='show_drink_order_view'),
    url(r'drink_orders/update/(?P<pk>\d+)/$', UpdateDrinkOrder.as_view(), name='update_drink_order_view'),
    url(r'customers/$', PendingCustomers.as_view(), name='pending_customers_view'),
    url(r'customer_order/(?P<pk>\d+)/$', ShowCustomerOrder.as_view(), name='show_customer_order_view'),

]
