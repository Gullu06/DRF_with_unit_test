from rest_framework import serializers

class IncomeSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField(default = 1)
    bank_name = serializers.CharField(max_length=100)
    annual_income = serializers.IntegerField()
    investment = serializers.IntegerField()
