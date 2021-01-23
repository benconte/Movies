from django.contrib import admin
from .models import Genres, Movies, Tv_shows, Tv_shows_seasons, Tv_shows_episodes, Popular_movies, popular_tv_shows

# Register your models here.
admin.site.register(Genres)
admin.site.register(Movies)
admin.site.register(Tv_shows)
admin.site.register(Tv_shows_seasons)
admin.site.register(Tv_shows_episodes)
admin.site.register(Popular_movies)
admin.site.register(popular_tv_shows)
