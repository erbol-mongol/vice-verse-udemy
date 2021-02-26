from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request , 'index.html')
    
def reverse(request):
    user_text = request.GET['textarea']
    return render(request , 'reverse.html', {'user_text': user_text[::-1]})