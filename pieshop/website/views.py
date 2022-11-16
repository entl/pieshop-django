from django.shortcuts import render
from django.forms import modelform_factory
from .models import Pie, Order
from .forms import OrderForm
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from django.http import JsonResponse


class Home(TemplateView):
    template_name = 'website/index.html'


class Contact(TemplateView):
    template_name = 'website/contact.html'


class Pies(ListView):
    model = Pie
    context_object_name = "pieList"
    template_name = 'website/pies.html'


class Order(CreateView):
    model = Order
    form_class = OrderForm
    template_name = "website/order.html"
    def get_success_url(self):
        return reverse_lazy('home')


# def home(request):
#     return render(request, 'website/index.html')


# def contact(request):
#     return render(request, 'website/contact.html')


# def pies(request):
#     pieList = Pie.objects.all()
#     return render(request, 'website/pies.html',
#                   {"pieList": pieList,})


# OrderForm = modelform_factory(Order, exclude=[])
# def order(request):
#     if request.POST:
#         pass
#     else:
#         form = OrderForm()
#     return render(request, 'website/order.html',
#                   {"form": form,})


