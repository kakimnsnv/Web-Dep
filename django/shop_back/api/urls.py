from django.urls import path
from api.views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('products/', product_list, name='product-list'),
    path('products/<int:id>/', product_detail, name='product-detail'),
    path('categories/', category_list, name='category-list'),
    path('categories/<int:id>/', category_detail, name='category-detail'),
    path('categories/<int:id>/products', category_products, name='category-products'),
]

urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)
