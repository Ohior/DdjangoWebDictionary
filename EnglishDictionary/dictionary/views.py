from django.shortcuts import render
# from EnglishDictionary import dictionary
from PyDictionary import PyDictionary

# Create your views here.


def index(request):
    return render(request, 'index.html')

def word(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()
    meanings = dictionary.meaning(search)
    synonyms = dictionary.synonym(search)
    antonyms = dictionary.antonym(search)
    context = {
        'meanings': meanings,
        'synonyms': synonyms,
        'antonyms': antonyms
    }
    return render(request, 'word.html', context)
