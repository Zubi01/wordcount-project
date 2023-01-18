from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def aboutpage(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext'] #store in a variable called fulltext
    #print(fulltext) #this will print in the cmd prompt
    wordlist = fulltext.split() #split up the strg into a list of the words inside and where theres a space it considers thats breaking apart 2 words

    worddictionary = {}

    for word in wordlist: #to loop the items in the dictionary above
        if word in worddictionary:
            #increase
            worddictionary[word] += 1
        else:
            #add to the dictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)  #to sort items. #1 look at the values in count(not cont which is 0). Reverse says what order you want to sort. Assign to a variable 'sortedwords'

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwords})#dictionary returns fulltext variable.#.item converts dictionary to a list
