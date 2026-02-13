from django.shortcuts import render

def prime(request):
    return render(request, 'prime.html')