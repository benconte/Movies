from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('home_copy', views.home_copy, name="home_copy"),
    path('trending', views.trending_now, name="trending"),
    path('en', views.home_start_page, name="home_start_page"),
    path('search', views.search, name="search"),
    path('copy_flix/<int:id>', views.copy_flix, name="copy_flix"),
    path('like/<int:id>', views.like_movie, name="like_movie"),
	path('favorite/<int:id>', views.favorite_movie, name="favorite_movie"),
    path('show_favorite', views.show_favorite, name="show_favorite"),
    path('en', views.home_start_page, name="home_start_page"),
    path('Watch_movie/<int:id>', views.show_movie_data, name="show_movie_data"),
    path('Tv_show/<int:id>', views.show_tv_shows_data, name="show_tv_shows_data"),
    path('Tv_series/<int:id>', views.display_tv_show, name="play_tv_show"),
    path('Watch/<int:id>', views.watch_tv_show, name="watch_tv_show"),
    path('Genres/<int:genre>', views.show_genres_movies, name="show_genres_movies"),
]
