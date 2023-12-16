from django.shortcuts import render
from .models import Income
from .serializers import IncomeSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.
def income_details(request, pk):
    income_data = Income.objects.get(customer_id = pk)
    # print(income_data)
    serializer = IncomeSerializer(income_data)
    # print(serializer)
    json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    return HttpResponse(json_data, content_type='application/json')

def income_list(request):
    income_data = Income.objects.all()
    # print(income_data)
    serializer = IncomeSerializer(income_data, many=True)
    # print(serializer)
    json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    return HttpResponse(json_data, content_type='application/json')
