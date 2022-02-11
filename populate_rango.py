import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tango_with_django_project.settings')

import django
django.setup() #always do this first

from rango.models import Category, Page

def populate():
    #1. create lists of dictionaries containing pages we want to add into each category
    #2. create a dictionary of dictionaries for our categories
    # - allows us to iterate through each data structure, and add the data to our models.

    python_pages = [
        {'title': 'Official Python Tutorial',
         'url':'http://docs.python.org/3/tutorial/',
         'views': 15},
        {'title': 'How to Think like a Computer Scientist',
         'url':'http://www.greenteapress.com/thinkpython/',
         'views': 10},
        {'title': 'Learn Python in 10 Minutes',
         'url':'http://www.korokithakis.net/tutorials/python/',
         'views': 24}]

    django_pages = [
        {'title':'Official Django Tutorial',
        'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'views': 12},
        {'title':'Django Rocks',
         'url':'http://www.djangorocks.com/',
         'views': 6},
        {'title':'How to Tango with Django',
         'url':'http://www.tangowithdjango.com/',
         'views': 13}]

    other_pages = [
        {'title':'Bottle',
         'url':'http://bottlepy.org/docs/dev/',
         'views': 5},
        {'title':'Flask',
         'url':'http://flask.pocoo.org',
         'views': 7}]

    cats = [
        {"name": 'Python',
        "pages": python_pages,
        "views": 128,
        "likes": 64},
    
        {"name": 'Django',
        "pages": django_pages,
        "views": 64,
        "likes": 128},
        
        {"name":'Other Frameworks',
        "pages": other_pages,
        "views": 32,
        "likes": 16}]

    for cat in cats:          #goes through cats dict
        c = add_cat(cat['name'], cat['views'], cat['likes'])
        for p in cat['pages']:     
            add_page(c, p['title'], p['url'], p["views"])   #adds associated pages for that category


    for c in Category.objects.all():            #prints categories added
        for p in Page.objects.filter(category = c):
            print(f'- {c}: {p}')


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.likes = likes
    c.views = views
    c.save()
    return c

if __name__ == '__main__':                      #begin execution
    print('Starting Rango population script...')
    populate()
            
