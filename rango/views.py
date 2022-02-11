from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page

# Create your views here.

def index(request):
    category_list = Category.objects.order_by('-likes')[:5] #top 5


    
    #Construct a dictionary to pass to the template engine as its context
    #Note the key boldmessage matches to {{boldmessage}} in the template
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list

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

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)

        pages = Page.objects.filter(category = category)        #retrieve associated pages

        context_dict['pages'] = pages                           #add results list to template context

        context_dict['category'] = category

    except Category.DoesNotExist:
        #exception handling if we co uldn't find specified category
        context_dict['category'] = None
        context_dict['pages'] = None
        
    return render(request, 'rango/category.html', context = context_dict)
        
        

        
