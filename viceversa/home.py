from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request , 'index.html')
    
def reverse(request):
    user_text = request.GET['textarea']
    amount_of_words = user_text.count(' ')
    return render(request , 'reverse.html', {'user_text': user_text , "reversed_text" : user_text[::-1] , "amount_of_words": amount_of_words})