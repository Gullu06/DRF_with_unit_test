from django.contrib import admin
from django.urls import path
from django_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('incomeinfo/<int:pk>/', views.income_details),
    path('incomeinfo/', views.income_list),
]
