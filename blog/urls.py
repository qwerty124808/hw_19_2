from django.urls import path
from blog.views import BlogCreateView, BloglistView, BlogDetailView, BlogUpdateView, BlogDeleteView
from blog.apps import BlogConfig
app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('blogs/', BloglistView.as_view() , name='list'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete')
]