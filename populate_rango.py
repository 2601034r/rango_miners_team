import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.

    python_pages = [
        {'title': 'Learn Python 2',
        'url':'https://www.codecademy.com/learn/learn-python',
        'views': 69},
        {'title':'Learn Python in 1 Hour',
        'url':'https://www.youtube.com/watch?v=ie-hjFXlxTs',
        'views': 800},
        {'title':'Python Tutorial for Beginners',
        'url':'https://www.youtube.com/watch?v=mJEpimi_tFo',
        'views': 162},
        {'title':'Complete Python Course',
        'url':'https://edube.org/?gclid=EAIaIQobChMI8qHj15-d8gIVFFZgCh27Zg4zEAAYBCAAEgKZc_D_BwE',
        'views': 187},
        {'title':'Official Python Tutorial',
        'url':'https://www.python.org/about/gettingstarted/',
        'views': 89}
        ]

    django_pages = [
        {'title':'Official Django Tutorial',
        'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
        'views': 40},
        {'title':'Getting Started with Django',
        'url':'https://www.djangoproject.com/start/',
        'views': 10},
        {'title':'Django Tutorial',
        'url':'https://www.geeksforgeeks.org/django-tutorial/',
        'views': 163},
        {'title':'Django Tutorial For Beginners',
        'url':'https://www.youtube.com/watch?v=OTmQOjsl0eg',
        'views': 163}
         ]

    other_pages = [
        {'title': 'Learn Data Science In Under 3 Hours',
        'url':'https://www.youtube.com/watch?v=aGu0fbkHhek',
        'views': 900},
        {'title':'Data Science For Beginners',
        'url':'https://www.javatpoint.com/data-science',
        'views': 64},
        {'title':'Data Science Tutorials',
        'url':'https://www.datacamp.com/community/tutorials',
        'views': 84},
        {'title':'A Path To Becomming a Data Scientist',
        'url':'https://intellipaat.com/blog/tutorial/data-science-tutorial/',
        'views': 648},
        {'title':'Intro To Data Science',
        'url':'https://www.udacity.com/course/intro-to-data-science--ud359',
        'views': 23},
        {'title':'Statistics and R For Data Science',
        'url':'https://online-learning.harvard.edu/course/statistics-and-r?delta=2',
        'views': 34}
        ]

    cats = {'Python': {'pages': python_pages, 'views' : 128, 'likes' : 64},'Django': {'pages': django_pages, 'views' : 64, 'likes' : 32},'Other Frameworks': {'pages': other_pages, 'views' : 32, 'likes' : 16} }

    # If you want to add more categories or pages,
    # add them to the dictionaries above.

    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.
    for cat, cat_data in cats.items():
        c = add_cat(cat, views=cat_data['views'], likes=cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], views=p['views'])

    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views=views
    c.likes=likes
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
