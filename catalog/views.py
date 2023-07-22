from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView, 
                                  DetailView, 
                                  TemplateView, 
                                  CreateView, 
                                  UpdateView, 
                                  DeleteView)
from catalog.admin import Category, Product
from catalog.models import Version
from django.urls import reverse_lazy, reverse
from catalog.forms import ProductForm, VersionForm
from django.forms import inlineformset_factory
from django.db import transaction

class HomeView(ListView):
    model = Product
    template_name = "catalog/home.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        version_list = Version.objects.all()
        context_data['formset'] = version_list
        return context_data


class ContactsViw(TemplateView):
    template_name = "catalog/contacts.html"


class CategoryListView(ListView):
    model = Category
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        return queryset


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:category")

    def get_queryset(self, *args, **kwargs):
        product_name = self.request.GET.get("product_name")
        if product_name == "казино":
            success_url = reverse_lazy("catalog:home")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(self.model, Version, form=VersionForm, extra=1)
        if self.request.method =="POST":
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        with transaction.atomic():
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:category")


class ProductListView(ListView):
    model = Product

    def get_queryset(self, *args, **kwargs):
        category_id = self.request.GET.get("category_id")
        return Product.objects.filter(category=category_id)


class ProductDetail(DetailView):
    model = Product