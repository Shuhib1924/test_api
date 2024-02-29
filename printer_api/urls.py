from django.urls import path
from . import views
urlpatterns = [
    path('', views.test, name='test'),
    path('<int:pk>/', views.single_order, name='single_order')
]