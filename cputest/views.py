from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cpu_test(request):
    i = 0
    
    while i < 100000000:
        test = 100 * 100 / 12
        test += 1
        i += 0
        
    return HttpResponse("Ending")