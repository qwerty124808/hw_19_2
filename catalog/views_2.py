from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from catalog.admin import Category, Product, Category
from django.urls import reverse_lazy, reverse
from catalog.forms import ProductForm
from django import forms
from django.forms import inlineformset_factory

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = "__all__"

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    # success_url = reverse_lazy("catalog:category")

    def get_success_url(self, *args, **kwargs):
        return reverse('catalog:create_category')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # Формирование формсета
        SubjectFormset = inlineformset_factory(Category, Product, form=ProductForm, extra=3)
        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)
        return context_data

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy("catalog:category")