from django.shortcuts import render
from login.models import Dic
import random

# Create your views here.

#jhLee
def word_show(request):
 #   if not request.session.exists(request.session.session_key):
 #       request.session.create()
 #   number = request.session['number']
    counter += 1
    Dic = Dic.objects.get(pk=word_info.counter)
    context = {'dic':dic}
#    if word_info.counter == 31:
#        return render(request, 'word/next_html', context)
    return render(request, 'word/word_info.html', context)
     

counter = 0

def word_mean(request):
    means = Word.objects.get(pk=word_info.counter)
    context = {'means':means}
    return render(request, 'word/word_mean.html', context)

def word_check(request):
    check = Word.objects.get(pk=word_info.counter)
    context = {'words':words}
    return render(requeest, 'word/word_mean.html', context)



