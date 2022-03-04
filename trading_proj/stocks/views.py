from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def home_view(request):
    url = "https://yfapi.net/v6/finance/quote"
    querystring = {"symbols":"AAPL,BTC-USD,EURUSD=X"}
    headers = {
    'x-api-key': "YOUR-PERSONAL-API-KEY"
    }
    data = requests.get(url).json()
    # data = requests.request("GET", url, headers=headers, params=querystring)
    # print(data.text)
    return HttpResponse(data)