from django.urls import path
from .views import CustomUserList, CustomerDetail, ProductList, ProductDetail, OrderList, OrderDetailView, OrderDetailList, OrderDetailDetailView

urlpatterns = [
    path('customers/', CustomUserList.as_view()),
    path('customers/<int:pk>/', CustomerDetail.as_view()),
    path('products/', ProductList.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
    path('orders/', OrderList.as_view()),
    path('orders/<int:pk>/', OrderDetailView.as_view()),
    path('order-details/', OrderDetailList.as_view()),
    path('order-details/<int:pk>/', OrderDetailDetailView.as_view()),
]
