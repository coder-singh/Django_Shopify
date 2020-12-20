from django.shortcuts import render, HttpResponse
import requests
import json
from django.conf import settings

# Create your views here.
def list_customers(request):
    '''
    list_customers view fetches first 50 customers from shopify GraphQL
    And render in customers.html
    '''

    query="""query {
    customers(first: 50) {
        edges {
        node {
            id
            firstName
            lastName
            email
            ordersCount
            tags
        }
        }
    }
    }"""

    url = 'https://{}:{}@shoptrade-labs.myshopify.com/admin/api/2020-10/graphql.json'.format(settings.API_KEY, settings.API_PASS)

    r = requests.post(url, json={'query': query})

    data = json.loads(r.text)['data']['customers']['edges']
    
    template = 'customers.html'
    context = {
        'data': data
    }
    return render(request, template, context)

def update_customer(request):
    '''
    This view takes an ajax request and sends put request to shopify REST API
    '''
    user_id = request.POST.get('user_id')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    tags = request.POST.get('tags').split(',')
    print(tags)
    
    url = 'https://{}:{}@shoptrade-labs.myshopify.com/admin/api/2020-10/customers/{}.json'.format(settings.API_KEY, settings.API_PASS, user_id)
   
    payload = {
        "customer":{
            "id": user_id,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "tags": tags
        }
    }
    response = requests.put(url, json=payload, headers = {"Accept": "application/json", "Content-Type": "application/json"})
    print(response.text)
    return HttpResponse(response.status_code);