from django.urls import path
from catalog.views import HomeView, ContactsViw, ProductDetail, CategoryListView, ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView
from catalog.views_2 import CategoryCreateView, CategoryDeleteView
from catalog.apps import CatalogConfig
app_name = CatalogConfig.name

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('contacts/', ContactsViw.as_view(), name="contacts"),
    path("category/", CategoryListView.as_view(), name="category"),
    path('products/category/', ProductListView.as_view()),
    path('products/product/<int:pk>/', ProductDetail.as_view(), name="view"),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),
    path('createcategory/', CategoryCreateView.as_view(), name="create_category"),
    path('deletecategory/<int:pk>', CategoryDeleteView.as_view(), name="delete_category")

]