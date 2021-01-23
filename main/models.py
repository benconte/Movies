from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Genres(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return f"Genres ({self.name})"

class Movies(models.Model):
	genre = models.ForeignKey(Genres, on_delete=models.CASCADE, null=True, related_name="movie_genre")
	name = models.CharField(max_length=200)
	movie_image = models.ImageField(upload_to="movie_images", blank=True)
	movie = models.FileField(upload_to="movie_path", blank=True)
	description = models.TextField(null=True)
	author = models.CharField(max_length=200)
	date_released = models.DateTimeField(default=timezone.now)
	likes = models.ManyToManyField(User, related_name="movie_like", blank=True)
	favorites = models.ManyToManyField(User, related_name="movie_favorites", blank=True)

	def __str__(self):
		return f"Movies('{self.genre.name}, {self.name}','{self.author}', '{self.date_released}')"

	def total_likes(self):
		return self.likes.count()

	def total_favorites(self):
		return self.favorites.count()

	def get_absolute_url(self):
		return reverse('home')

class Tv_shows(models.Model):
	name = models.CharField(max_length=200)
	tv_show_image = models.ImageField(upload_to="tv_shows_images", blank=True)
	genre = models.ForeignKey(Genres, on_delete=models.CASCADE, null=False)
	date_released = models.DateTimeField(default=timezone.now)
	Tv_shows_description = models.TextField(null=True)

	def __str__(self):
		return f"Tv_show({self.name})"

	@property
	def tv_show_image_url(self):
	    if self.tv_show_image and hasattr(self.tv_show_image, 'url'):
	        return self.tv_show_image.url

class Tv_shows_seasons(models.Model):
	tv_show = models.ForeignKey(Tv_shows, on_delete=models.CASCADE, null=False, related_name='Tv_shows_seasons')
	name = models.CharField(max_length=200)
	reference_name = models.CharField(max_length=200, null=True)
	tv_show_image = models.ImageField(upload_to="tv_shows_seasons_images", blank=True)
	date_released = models.DateTimeField(default=timezone.now)
	Tv_shows_description = models.TextField(null=True)

	def __str__(self):
		return f"Tv_show({self.tv_show.name} ,{self.name})"

class Tv_shows_episodes(models.Model):
	genre = models.ForeignKey(Genres, on_delete=models.CASCADE, null=True, related_name="Tv_shows_episodes_genre")
	tv_show = models.ForeignKey(Tv_shows_seasons, on_delete=models.CASCADE, null=False, related_name="Tv_shows_episodes")
	name = models.CharField(max_length=200)
	reference_name = models.CharField(max_length=200, null=True)
	Tv_show_image = models.ImageField(upload_to="movie_images", blank=True)
	Tv_show_path = models.FileField(upload_to="movie_path", blank=True)
	episode_description = models.TextField(null=True)
	# author = models.CharField(max_length=200)
	date_released = models.DateTimeField(default=timezone.now)
	likes = models.ManyToManyField(User, related_name="tv_show_like", blank=True)
	favorites = models.ManyToManyField(User, related_name="tv_show_favorites", blank=True)

	def __str__(self):
		return f"Tv_shows_movies('{self.tv_show.tv_show.name}','{self.tv_show.name}', '{self.name}')"
		# the tv_show.tv_show gets the tv_show from the tv_shows_seasons from there gets it name

	def total_likes(self):
		return self.likes.count()

	def get_absolute_url(self):
		return reverse('home')



# creating classes for movies to display in home pages and trendings and others
class Popular_movies(models.Model):
	genre = models.ForeignKey(Genres, on_delete=models.CASCADE, null=True, related_name="popula_movie_genre")
	movie = models.ForeignKey(Movies, on_delete=models.CASCADE, null=True, related_name="popular_movie")
	

	def __str__(self):
		return f"Popular_movies('{self.movie.name}','{self.movie.author}', '{self.movie.date_released}')"

	def get_absolute_url(self):
		return reverse('home')

class popular_tv_shows(models.Model):
	genre = models.ForeignKey(Genres, on_delete=models.CASCADE, null=True, related_name="tv_show_genre")
	tv_show = models.ForeignKey(Tv_shows, on_delete=models.CASCADE, null=True, related_name="tv_show")
	

	def __str__(self):
		return f"popular_tv_shows('{self.tv_show.genre.name}', '{self.tv_show.name}', '{self.tv_show.date_released}')"

	def get_absolute_url(self):
		return reverse('home')