from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

data = []
# Create your views here.
@csrf_exempt
def values(request):
    if request.method == 'POST':
        data.append(json.loads(json.dumps({"temperature": json.loads((request.body).decode('utf-8')).get('temperature'), "humidity": json.loads((request.body).decode('utf-8')).get('humidity')})))
        return JsonResponse(data, safe=False)
    if request.method == 'GET':
        #data = json.loads(json.dumps((request.POST['temperature'])))
        return JsonResponse(data, safe=False)
# return HttpResponse(request,data)

def gui(request):
    if request.method == 'GET':
        return render(request,'main.html')