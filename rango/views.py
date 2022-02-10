from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #Construct a dictionary to pass to the template engine as its context
    #Note the key boldmessage matches to {{boldmessage}} in the template
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    #Return a rendered response to the client
    #Shortcut function makes life easier
    #First parameter is the template we wish to use.

    return render(request, 'rango/index.html', context = context_dict)
    
    ##hyperlink = '<a href="/rango/about.">About</a>'
    ##return HttpResponse(hyperlink+" Rango says hey there partner!")

def about(request):
    hyperlink = '<a href="/rango/index.html.">Index</a>'
    context_dict = {'boldmessage':" This tutorial has been put together by John Wilson"}
    
    return render(request, 'rango/about.html', context = context_dict)
