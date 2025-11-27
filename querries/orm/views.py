from django.shortcuts import render
from .models import Movie, Viewer, Review

def hello(request):
    movie_exact = Movie.objects.filter(title__exact = 'IT')
    viewers_contains_lastname = Viewer.objects.filter(surname__contains = 'Star')
    genre_starts = Movie.objects.filter(genre__startswith = 'psychological')
    email_ends = Viewer.objects.filter(email__endswith = '@gmail.com')
    
    long_movies = Movie.objects.filter(duration_minutes__gt = 120)
    high_score_reviews = Review.objects.filter(score__gte = 8)
    low_rating_movies = Movie.objects.filter(rating__lt = 5)
    young_viewers = Viewer.objects.filter(age__lte = 18)
    medium_length_movies = Movie.objects.filter(duration_minutes__range=(90, 150))

    movies_in_list = Movie.objects.filter(id__in = [1, 4, 6])
    reviews_without_viewer = Review.objects.filter(viewer__isnull = True)
    


    context = {
        'movie_exact': movie_exact,
        "viewers_contains_lastname": viewers_contains_lastname,
        "genre_starts": genre_starts,
        "email_ends": email_ends,
        "long_movies": long_movies,
        "high_score_reviews": high_score_reviews,
        "low_rating_movies": low_rating_movies,
        "young_viewers": young_viewers,
        "medium_length_movies": medium_length_movies,
        "movies_in_list": movies_in_list,
        "reviews_without_viewer": reviews_without_viewer
    }

    return render(request, 'base.html', context)