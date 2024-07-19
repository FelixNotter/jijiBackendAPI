from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.allProducts ),
    path('products/<int:_id>/', views.getProduct ),
    path('carts/', views.allCarts ),
    path('carts/<int:_id>/', views.updateCart ),
    path('quantity/<int:_id>/', views.getStock ),
    path('addcart/', views.createCart ),
]