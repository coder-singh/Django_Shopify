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