from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from catalog.admin import Category, Product

class HomeView(ListView):
    model = Product
    template_name = "catalog/home.html"

# def home(request):
#     product_id = request.GET.get('product_id')
#     products_list = Product.objects.all()
#     context = {
#         'products_list': products_list
#     }
#     return render(request, 'catalog/home.html', context)

# class ContactsView(DetailView):
#     template ="catalog/contacts.html"

class ContactsViw(TemplateView):
    template_name = "catalog/contacts.html"

# def contacts(request):
#     return render(request, 'catalog/contacts.html')

class CategoryListView(ListView):
    model = Category
    template_name = "catalog/category.html"

# def category(request):
#     category_list = Category.objects.all()
#     context = {
#         'object_list': category_list
#     }
#     return render(request, 'catalog/category.html', context)

class ProductListView(ListView):
    model = Product
    template_name = "catalog/produkts.html"
    def get_queryset(self, *args, **kwargs):
        category_id = self.request.GET.get("category_id")
        return Product.objects.filter(category=category_id)

# def products(request):
#     # request= http://127.0.0.1:8000/category/?category_id=1
#     category_id = request.GET.get("category_id")
#     products_list = Product.objects.filter(category=category_id)
    
#     context = {
#         'products_list': products_list
#     }
#     return render(request, 'catalog/produkts.html', context)

class ProductDetail(DetailView):
    model = Product
    template_name = "catalog/product_info.html"

# def product_info(request, pk):
#     product_id = request.GET.get('product_id')
#     item = Product.objects.filter(id=product_id).first()
#     # item = get_object_or_404(Product, id=product_id)   
#     context = {
#         'item': item
#     } 
#     return render(request, 'catalog/product_info.html', context)