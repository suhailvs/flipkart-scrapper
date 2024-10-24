from django.urls import include, path, re_path
from . import views

app_name = 'myapp'
urlpatterns = [
	path('', views.products, name='products'),
    path('p/<int:f>/', views.parse_products, name='parse_products'),
    
]