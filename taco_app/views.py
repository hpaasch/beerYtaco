from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from taco_app.models import CustomerOrder, OrderLine

class IndexView(CreateView):
    template_name = 'index.html'
    model = OrderLine
    fields = ['order', 'food', 'drink', 'extra', 'notes', 'quantity']
