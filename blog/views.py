from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from blog.models import Blog
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify

class BlogCreateView(CreateView):
    model = Blog
    fields = ('heading', 'content', 'picture', 'is_published')
    success_url = reverse_lazy("blog:list")

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save() 
            new_blog.slug = slugify(new_blog.heading)
            new_blog.save()

        return super().form_valid(form)

    

class BloglistView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset

class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('heading', 'slug', 'content', 'picture', 'is_published')
    # success_url = reverse_lazy("blog:list")

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save() 
            new_blog.slug = slugify(new_blog.heading)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:list")