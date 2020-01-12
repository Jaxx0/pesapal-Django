from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('', views.home, name='home'),
    path('payment/', views.payment, name='pay'),
    path('payment/oauth_callback/', views.callback, name='callback'),
]