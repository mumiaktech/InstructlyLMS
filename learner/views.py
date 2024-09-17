from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from instructor.models import Resource
import requests
from django.utils.dateparse import parse_datetime
import environ

# Initialize environment variables
env = environ.Env()

#home view
@login_required
def student_home(request):
    return render(request, 'student/student_home.html')

#resurces view
@login_required
def student_resources(request):
    query = request.GET.get('q')
    if query:
        resources = Resource.objects.filter(title__icontains=query)
    else:
        resources = Resource.objects.all()
    
    context = {
        'resources': resources,
        'query': query,
    }
    return render(request, 'student/student_resources.html', context) 

#news view
@login_required
def news_view(request):
    api_key = env('NEWS_API_KEY')  # Use environment variable
    url = f'https://newsapi.org/v2/everything?q=education&from=2024-08-30&sortBy=publishedAt&apiKey={api_key}'

    response = requests.get(url)
    articles = response.json().get('articles', [])
    print(response.json())

    # Parse the publishedAt date
    for article in articles:
        published_at = article.get('publishedAt')
        if published_at:
            article['publishedAt'] = parse_datetime(published_at)

    context = {
        'articles': articles
    }

    return render(request, 'student/news.html', context)

#books view
@login_required
def books_view(request):
    query = request.GET.get('q', 'linux')  
    api_key = env('GOOGLE_API_KEY')  # Use environment variable  
    books = []

    if query:
        url = f'https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}'
        response = requests.get(url)

         # Debugging
        print(response.json())

        if response.status_code == 200:
            books = response.json().get('items', [])

    context = {
        'books': books,
        'query': query
    }
    
    return render(request, 'student/books.html', context)

#videos view
@login_required
def videos_view(request):
    api_key = env('GOOGLE_API_KEY')  # Use environment variable  
    query = request.GET.get('q', 'educational')  
    
    url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={query}&type=video&key={api_key}'
    
    response = requests.get(url)
    results = response.json().get('items', [])
    
    context = {
        'videos': results,
        'query': query,
    }
    
    return render(request, 'student/videos.html', context)
