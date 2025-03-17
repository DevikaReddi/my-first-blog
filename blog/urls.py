from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/new/', views.product_new, name='product_new'),
    path('product/<int:pk>/edit', views.product_edit, name='product_edit'),
    path('product/<int:pk>/delete', views.product_delete, name='product_delete'),
]
