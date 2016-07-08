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
