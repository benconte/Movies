from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Genres, Movies, Tv_shows, Tv_shows_seasons, Tv_shows_episodes, Popular_movies, popular_tv_shows
from math import ceil
# Create your views here.


def home_start_page(request):
	return render(request, "main/home_start_page.html", {})

@login_required
def copy_flix(request, id):
	movie = get_object_or_404(Movies, id=id)
	if movie:
		context = {
			'movie':movie
		}
		return render(request, 'main/copy_flix.html', context)
	else:
		messages.warning(request, 'Movie not found')
		return HttpResponseRedirect("/")

@login_required
def home(request):
	movies = Movies.objects.all()
	tv_shows = Tv_shows.objects.all()

	n = len(movies)
	# nSlides = n//4 + ceil((n/4) - (n//4))
	# allmovies = [[movies, range(1,nSlides),nSlides],[movies, range(1,nSlides),nSlides],[movies, range(1,nSlides),nSlides],[movies, range(1,nSlides),nSlides]]
	context={
		'allmovies':movies,
		'tv_shows':tv_shows
	}
	return render(request, "main/home.html", context)

@login_required
def home_copy(request):
	movies = Movies.objects.all()
	n = len(movies)
	context={
		'allmovies':movies
	}
	return render(request, "main/home_copy.html", context)

@login_required
def like_movie(request, id):
	movie = get_object_or_404(Movies, id=request.POST.get('movie_id'))#getting the book which takes the like
	liked = False
	if movie.likes.filter(id=request.user.id).exists():#check if the like has been liked by a specific user
		movie.likes.remove(request.user)
		liked = False
	else:
		movie.likes.add(request.user)
		liked = True

	return HttpResponseRedirect(reverse('show_movie_data', args=[str(id)]))

@login_required
def favorite_movie(request, id):
	movie = get_object_or_404(Movies, id=id)
	if movie.favorites.filter(id=request.user.id).exists():
		movie.favorites.remove(request.user)

	else:
		movie.favorites.add(request.user)

	return HttpResponseRedirect(reverse('show_movie_data', args=[str(id)]))


@login_required
def show_favorite(request):

	return render(request, 'main/favorites.html', {})


@login_required
def show_movie_data(request, id):
	movie = get_object_or_404(Movies, id=id)
	if movie:
		stuff = get_object_or_404(Movies, id=id)
		total_likes = stuff.total_likes()
		liked = False
		is_favorite = False

		if stuff.favorites.filter(id=request.user.id).exists():
			is_favorite = True

		
		if stuff.likes.filter(id=request.user.id).exists():
			liked = True

		context = {
			'movie':movie,
			'total_likes':total_likes,
			'liked': liked,
			'is_favorite': is_favorite,
		}
		return render(request, 'main/show_movie_data.html', context)
	else:
		messages.warning(request, 'Movie not found')
		return HttpResponseRedirect("/")



@login_required
def show_tv_shows_data(request, id):
	tv_show_genre = get_object_or_404(Tv_shows, id=id)

	context = {
		'tv_show':tv_show_genre,

	}
	return render(request, 'main/show_tv_show_data.html', context)

@login_required
def display_tv_show(request, id):
	tv_show_season = get_object_or_404(Tv_shows_seasons, id=id)

	context = {
		'tv_show_season':tv_show_season,

	}
	return render(request, 'main/play_tv_show.html', context)

@login_required
def watch_tv_show(request, id):
	# tv_show_season = get_object_or_404(Tv_shows_seasons, id=id)
	tv_show_episode = get_object_or_404(Tv_shows_episodes, id=id)

	context = {
		'tv_show_season':tv_show_episode.tv_show,
		'tv_show_episode':tv_show_episode

	}
	return render(request, 'main/watch_tv_show.html', context)


@login_required
def show_genres_movies(request, genre):
	get_genre = Genres.objects.get(id=genre)

	if get_genre:
		
		context = {
			'genre_movies':get_genre
		}
		return render(request, "main/show_genres_movies.html", context)
	else:
		messages.warning(request, "Genre not found!!")
		return HttpResponseRedirect('/')



@login_required
def search(request):
	if request.method == 'GET':
		query = request.GET.get('q')

		if query:
			match = Movies.objects.filter(name__icontains=query)
			sec_match = Tv_shows.objects.filter(name__icontains=query)
			

			if match or sec_match:
				max_results_match = len(match)
				max_results_sec_match = len(sec_match)
				print("Match found")
				context = {
					'query_result':match,
					'max_results':max_results_match,
					'sec_match':sec_match,
					'max_results_sec_match':max_results_sec_match

				}
				return render(request, 'main/search.html', context)
			else:
				messages.warning(request, "No results found.Try searching with the name of the movie, tv shows, tv series and more")
				return HttpResponseRedirect("/")

		else:
			messages.warning(request, "The search field can't be empty.Try searching for a movie or a show")
			return HttpResponseRedirect("/")

	return HttpResponseRedirect("/")


def trending_now(request):
	popular_movies = Popular_movies.objects.all()
	movies = Movies.objects.all()
	pop_tv_shows = popular_tv_shows.objects.all()

	context = {
		'movies': movies,
		'popular_movies':popular_movies,
		'popular_tv_shows':pop_tv_shows
	}
	return render(request, 'main/trending_now.html', context)