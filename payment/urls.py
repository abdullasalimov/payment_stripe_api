from django.urls import path
from payment.views import index


urlpatterns = [
    path("", index, name='index'),
]
