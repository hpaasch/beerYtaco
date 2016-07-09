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
    model = Customer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = self.kwargs.get('pk', None)
        food_list = OrderFood.objects.filter(order_tag_id=customer).filter(order_tag_id__paid=False)
        total_unpaid = 0
        for food in food_list:
            total_unpaid += (food.food.price * food.food_quantity)
        drink_list = OrderDrink.objects.filter(order_tag_id=customer).filter(order_tag_id__paid=False)
        for drink in drink_list:
            total_unpaid += (drink.drink.price * drink.drink_quantity)
        context = {
            'food_list': food_list,
            'drink_list': drink_list,
            'total_unpaid': total_unpaid,
        }
        return context
