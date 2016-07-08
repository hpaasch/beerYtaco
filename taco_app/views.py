from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from taco_app.models import Customer, OrderFood, OrderDrink, Food
from django.core.urlresolvers import reverse_lazy


class IndexView(ListView):
    template_name = 'index.html'
    model = Food


class OrderFoodView(CreateView):
    template_name = 'order_food.html'
    model = OrderFood
    fields = ['order_tag', 'food', 'food_quantity', 'extra', 'extra_quantity', 'notes', 'order_up']
    success_url = reverse_lazy('order_food_view')


class OrderDrinkView(CreateView):
    template_name = 'order_drink.html'
    model = OrderDrink
    fields = ['order_tag', 'drink', 'drink_quantity', 'notes', 'order_up']
    success_url = reverse_lazy('order_drink_view')

class ShowFoodOrder(ListView):
    template_name = 'show_food_order.html'
    model = OrderFood

    def get_queryset(self):
        return OrderFood.objects.filter(order_up=False)


class ShowDrinkOrder(ListView):
    template_name = 'show_drink_order.html'
    model = OrderDrink

    def get_queryset(self):
        return OrderDrink.objects.filter(order_up=False)


class ShowCustomerOrder(ListView):
    template_name = 'show_customer_order.html'

    def get_queryset(self, **kwargs):
        customer = self.kwargs.get('pk', None)
        OrderDrink.objects.filter(order_tag__tag_number=customer.tag_number)
