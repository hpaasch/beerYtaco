
from django.conf.urls import url, include
from django.contrib import admin

from taco_app.views import IndexView, OrderFoodView, OrderDrinkView, ShowFoodOrder

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    # url(r'^create_account/$', CreateAccountView.as_view(), name='create_account_view'),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'food/$', OrderFoodView.as_view(), name='order_food_view'),
    url(r'drink/$', OrderDrinkView.as_view(), name='order_drink_view'),
    url(r'order/$', ShowFoodOrder.as_view(), name='show_food_order_view'),
]
