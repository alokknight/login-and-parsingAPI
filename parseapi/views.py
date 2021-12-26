from django.shortcuts import render
import requests
import json
import pandas as pd
# Create your views here.

def parseapi(request):
    api= requests.get('https://s3.amazonaws.com/open-to-cors/assignment.json')
    print(api.status_code)
    data = api.text

    # storing the JSON response from url in data
    parse_json = json.loads(data)

    # count = parse_json['count']
    # print(count)

    products = parse_json['products']
    # print(products)
    # print(type(products))
    data=[]
    for key in products:
        x=products[key]
        data.append(x)
    # print(data)
    df = pd.DataFrame.from_dict(data)
    df.sort_values(by=['popularity'])
    context=[]
    for index, row in df.iterrows():
        x=row['subcategory']
        y=row['title']
        z=row['price']
        za=row['popularity']
        con={'x':x,'y':y,'z':z,'za':za}
        context.append(con)
    print(context)
    print(type(context))
    return render(request, 'parseapi/parseapi.html',{'context':context})


# def index(request):
#     context= {}#request.POST.get('context')
#     return render(request,"account/index.html",context)
