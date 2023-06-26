from django.urls import path
from catalog.views import home, contacts

urlpatterns = [
    path('home/', home),
    path('contacts/', contacts)

]