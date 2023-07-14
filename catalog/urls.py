from django.urls import path
from catalog.views import HomeView, ContactsViw, ProductDetail, CategoryListView, ProductListView
from catalog.apps import CatalogConfig
app_name = CatalogConfig.name

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('contacts/', ContactsViw.as_view(), name="contacts"),
    path("category/", CategoryListView.as_view(), name="category"),
    path('products/category/', ProductListView.as_view()),
    path('products/product/<int:pk>/', ProductDetail.as_view())

]