from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Persons
import csv
# Create your views here.
def homeview(request):
    return render (request, 'index.html')

def downloadpage(request):
    return render(request,'download.html')

def getasjson(request):
    data = Persons.objects.all()
    data_json = [{'firstname':person.Firstname,'surname':person.Surname, 'age':person.Age}for person in data]
    #return JsonResponse({'Persons':data_json})
    response = HttpResponse(content_type='text/csv')
    response['content-Disposition'] = 'attachment;filename="persons.csv"'
    csv_columns = ["Firstname","Surname", "Age"]
    writer = csv.DictWriter(response,fieldnames=csv_columns)
    writer.writeheader()
    for person in data:
        writer.writerow({'Firstname':person.Firstname, 'Surname':person.Surname, 'Age':person.Age})

    return response

    



