from django.shortcuts import render

# Create your views here.
def word_info(request):
    return render(request, 'word/word_info.html', {})