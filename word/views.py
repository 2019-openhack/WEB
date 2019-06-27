from django.shortcuts import render
from .models import Word

# Create your views here.
def word_info(request):
    words = Word.objects.all()
    context = {'words':words}
    return render(request, 'word/word_info.html', context)

def word_mean(request):
    means = Word.objects.all()
    context = {'means':means}
    return render(request, 'word/word_mean.html', context)
