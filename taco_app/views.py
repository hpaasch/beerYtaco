from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView
from taco_app.models import Customer, OrderFood, OrderDrink, Food
from django.core.urlresolvers import reverse_lazy

from taco_app.forms import OrderDrinkForm

class IndexView(ListView):
    template_name = 'index.html'
    model = Food


class OrderFoodView(CreateView):
    template_name = 'order_food.html'
    model = OrderFood
    fields = ['order_tag', 'food', 'food_quantity', 'extra', 'extra_quantity', 'notes', 'order_up']
    success_url = reverse_lazy('order_food_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_drink'] = OrderDrinkForm
        return context


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


class UpdateDrinkOrder(UpdateView):
    model = OrderDrink
    fields = ['order_up']
    success_url = reverse_lazy('show_drink_order_view')

    def get_object(self, queryset=None):
        drink = self.kwargs.get('pk', None)
        return OrderDrink.objects.get(pk=drink)


class ShowCustomerOrder(UpdateView):
    template_name = 'show_customer_order.html'
    model = Customer
    fields = ['paid']
    success_url = reverse_lazy('index_view')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = self.kwargs.get('pk', None)
        total_unpaid = 0
        subtotal_food = 0
        subtotal_drinks = 0
        food_list = OrderFood.objects.filter(order_tag_id=customer).filter(order_tag_id__paid=False)
        for food in food_list:
            subtotal_food += (food.food.price * food.food_quantity) + (food.extra.price * food.food_quantity)
        drink_list = OrderDrink.objects.filter(order_tag_id=customer).filter(order_tag_id__paid=False)
        for drink in drink_list:
            subtotal_drinks += (drink.drink.price * drink.drink_quantity)
        total_unpaid = subtotal_food + subtotal_drinks
        context = {
            'food_list': food_list,
            'drink_list': drink_list,
            'subtotal_food': subtotal_food,
            'subtotal_drinks': subtotal_drinks,
            'total_unpaid': total_unpaid,
            }
        return context

class PendingCustomers(ListView):
    model = Customer
    fields = ['tag_number', 'created']

    def get_queryset(self):
        return Customer.objects.filter(paid=False)
