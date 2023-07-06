from django.urls import path
from catalog.views import home, contacts, category, products, product_info

urlpatterns = [
    path('home/', home),
    path('contacts/', contacts),
    path("category/", category),
    path('products/', products),
    path('products/product/', product_info)

]