from django.urls import path
from product.models import Product
from . import views

urlpatterns = [
    # path('product/<str:name>', Product.DetailView.as_view(), name='product_detail'),
    path('list_product/', views.ListView.as_view(), name='product_list'),
    path('index/', views.HomePageView.as_view(), name='index'),
    path('lover/', views.MoneyLoverView.as_view(), name='lover'),
]
