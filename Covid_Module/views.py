from django.shortcuts import render
import json
import requests


url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "4090850c31msh46d394d3e2011a7p1c8928jsnd224c54c23c9"
    }

response = requests.request("GET", url, headers=headers).json()

def index(request):
    return render(request, 'base.html')

def getCountry(request):

    if(request.method =="POST"):
        noOfCountries = int(response['results'])
        country = request.POST['selectedCountry']
        countries = []

        for x in range(0, noOfCountries):
            if(country == response['response'][x]['country']):
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deadths = int(total) - int(active) - int(recovered)

        for i in range(0, noOfCountries):
            countries.append(response['response'][i]['country'])

        tempDict = {'country':country, 'countries': countries,'new': new, 'active':active,'critical':critical,'recovered':recovered,'total':total,'deaths':deadths}
        return render(request, 'Covid_Module/selectCountry.html', tempDict)
    
    noOfCountries = int(response['results'])
    countries = []

    for i in range(0, noOfCountries):
        countries.append(response['response'][i]['country'])
    
    tempDict = {'countries': countries}

    return render(request, 'Covid_Module/selectCountry.html', tempDict)
