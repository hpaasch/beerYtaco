
from django.conf.urls import url, include
from django.contrib import admin

from taco_app.views import IndexView, OrderFoodView, OrderDrinkView, ShowFoodOrder, ShowDrinkOrder, ShowCustomerOrder

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    # url(r'^create_account/$', CreateAccountView.as_view(), name='create_account_view'),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'food/$', OrderFoodView.as_view(), name='order_food_view'),
    url(r'drink/$', OrderDrinkView.as_view(), name='order_drink_view'),
    url(r'food_orders/$', ShowFoodOrder.as_view(), name='show_food_order_view'),
    url(r'drink_orders/$', ShowDrinkOrder.as_view(), name='show_drink_order_view'),
    url(r'customer_order/(?P<pk>\d+)/$', ShowCustomerOrder.as_view(), name='show_customer_order_view'),
]
