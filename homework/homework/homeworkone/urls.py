from django.urls import path
from . import views

urlpatterns = [
    path('product/1/', views.product, name='product'),
    path('product/2/', views.product_detail, name='product_detail')
]