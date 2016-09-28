from django.shortcuts import render

def app_addition(request):
    return render(request, 'apps/app_addition.html')
