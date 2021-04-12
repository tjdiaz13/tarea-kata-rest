from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .models import Portfolio
import json

# Create your views here.
@csrf_exempt
def index(request):
    portfolio_list = Portfolio.objects.all()
    return HttpResponse(serializers.serialize('json', portfolio_list))
