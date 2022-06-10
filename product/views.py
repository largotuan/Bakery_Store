from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, TemplateView

from product.models import Product


# def detail(request):
#     # order = get_object_or_404(Order, pk=order_id)
#     # context = {
#     #     'order': order,
#     #     'details': order.orderdetail_set.all()
#     # }
#     return render(request, 'product/list_product.html')


class ProductListView(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'products/list_product.html'


class HomePageView(TemplateView):
    template_name = 'product/index.html'


class MoneyLoverView(TemplateView):
    template_name = 'product/money_lover.html'

# def index(request):
#
#     context = {
#         'product': Product,
#         'details': Product.objects.all(),
#     }
#     return render(request, 'product/index.html', context)

