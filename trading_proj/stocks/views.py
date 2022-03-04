from django.shortcuts import render
from django.http import HttpResponse
import requests
import os

# Create your views here.
def home_view(request):
    var_key = "PERSONAL_API_KEY"
    url = "https://yfapi.net/v6/finance/quote"
    querystring = {"symbols":"AAPL,BTC-USD,EURUSD=X"}
    #take key from an environment variable
    personal_api = os.environ.get(var_key)
    headers = {
    'x-api-key': personal_api
    }
    # data = requests.get(url).json()
    data = requests.request("GET", url, headers=headers, params=querystring)
    # print(data.text)
    return HttpResponse(data)