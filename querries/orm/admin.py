from django.contrib import admin
from .models import Movie, Viewer, Review

admin.site.register(Movie)
admin.site.register(Viewer)
admin.site.register(Review)
