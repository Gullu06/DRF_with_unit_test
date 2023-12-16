from django.contrib import admin
from .models import Income
# Register your models here.
@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'bank_name', 'annual_income', 'investment']