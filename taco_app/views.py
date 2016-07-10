from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from taco_app.models import Customer, OrderFood, OrderDrink, Food, EmployeeProfile
from taco_app.forms import EmployeeProfileUpdateForm

class IndexView(ListView):
    template_name = 'index.html'
    model = Food


class OrderFoodView(CreateView):
    template_name = 'order_food.html'
    model = OrderFood
    fields = ['order_tag', 'food', 'food_quantity', 'extra', 'extra_quantity', 'notes']
    success_url = reverse_lazy('order_food_view')

    # this would put a second form on the template. but only one can be submitted at a time. darn.
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['order_drink'] = OrderDrinkForm
    #     return context


class OrderDrinkView(CreateView):
    template_name = 'order_drink.html'
    model = OrderDrink
    fields = ['order_tag', 'drink', 'drink_quantity', 'notes']
    success_url = reverse_lazy('order_drink_view')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['order_drink_form'] = OrderDrinkForm


class ShowFoodOrder(ListView):
    template_name = 'show_food_order.html'
    model = OrderFood

    def get_queryset(self):
        return OrderFood.objects.filter(order_up=False)


class ShowDrinkOrder(ListView):
    template_name = 'show_drink_order.html'
    model = OrderDrink
    fields = ['order_up']

    def get_queryset(self):
        return OrderDrink.objects.filter(order_up=False)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     drink = self.kwargs.get('pk', None)
    #     FINISH THIS TO TRY TO HAVE ORDER UP ON ONE CLICK


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
            if food.food_quantity >= 1:
                subtotal_food += (food.food.price * food.food_quantity)
        extras_list = OrderFood.objects.filter(order_tag_id=customer).filter(order_tag_id__paid=False)
        for extra in extras_list:
            if food.extra_quantity >= 1:
                subtotal_food += (food.extra.price * food.extra_quantity)
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


class CreateAccountView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('login')


class AccountProfileView(ListView):
    model = EmployeeProfile

    def get_object(self, queryset=None):
        return self.request.user.employeeprofile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = self.request.user
        context["nickname"] = self.request.user.employeeprofile.nickname
        context["role"] = self.request.user.employeeprofile.role
        context["preferred_language"] = self.request.user.employeeprofile.preferred_language
        return context


class EmployeeProfileUpdateView(UpdateView):
    model = EmployeeProfile
    success_url = reverse_lazy('account_profile_view')
    fields = ['nickname', 'role', 'preferred_language']

    def get_object(self, queryset=None):
        return self.request.user.employeeprofile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # if self.request.user.is_authenticated():
        context["profile_form"] = EmployeeProfileUpdateForm(initial={
            "nickname": self.request.user.employeeprofile.nickname,
            "role": self.request.user.employeeprofile.role,
            "preferred_language": self.request.user.employeeprofile.preferred_language,
        })
        # else:
        #     context["login_form"] = AuthenticationForm()
        return context
