from django.shortcuts import render
import requests
import json
# Create your views here.
def index(request):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '187fafe4-4b98-4bbd-8e90-5747c6ade20e',
    }
    params = {
    'start':'1',
    'limit':'5',
    'convert':'USD'
    }
    json=requests.get(url,params=params,headers=headers).json()
    coins=json['data']
    return render(request,'index.html',{'coins':coins})
