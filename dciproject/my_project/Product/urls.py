from django.urls import path
from .views import ProductListAPIView, ProductDetailAPIView
app_name = 'Product'

urlpatterns = [
    path('',ProductListAPIView.as_view(), name = 'product-list'),
    path('<str:product_name>', ProductDetailAPIView.as_view(),
         name = 'product_detail')
    
]