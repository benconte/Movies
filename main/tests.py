# from django.test import TestCase

# Create your tests here.

"""
	@login_required
def display_tv_show(request, reference_name):
	# tv_show_season = get_object_or_404(Tv_shows_seasons, id=id)
	tv_show_season = Tv_shows_seasons.objects.filter(reference_name=reference_name).first()

	context = {
		'tv_show_season':tv_show_season,

	}
	return render(request, 'main/play_tv_show.html', context)

@login_required
def watch_tv_show(request, name):
	# tv_show_season = get_object_or_404(Tv_shows_seasons, reference_name=reference_name)
	# tv_show_season = Tv_shows_seasons.objects.filter(name=name).first()
	tv_show_episode = Tv_shows_episodes.objects.filter(name=name).first()
	# tv_show_episode = get_object_or_404(Tv_shows_episodes, reference_name=reference_name)

	context = {
		'tv_show_season':tv_show_episode.tv_show,
		'tv_show_episode':tv_show_episode

	}
	return render(request, 'main/watch_tv_show.html', context)



# watch tv show

<a href="{% url 'watch_tv_show' tv_shw.name %}" style="text-decoration: none;">
                    <img src="{{tv_shw.Tv_show_image.url}}" width="60" height="60" style="float: left;margin: 5px;" id="img">
                    <button class="season-play-btn" value="{{tv_shw.Tv_show_path.url}}" id="play_button">Play Episode</button>
                    <p class="tv_show_name"><!-- {{tv_show_season.name}} : --> {{tv_shw.name}}</p>
                  </a>

# play tv show
 <a href="{% url 'watch_tv_show' tv_shw.name %}" style="text-decoration: none;">
                    <img src="{{tv_shw.Tv_show_image.url}}" width="60" height="60" style="float: left;margin: 5px;" id="img">
                    <button class="season-play-btn" value="{{tv_shw.Tv_show_path.url}}" id="play_button">Play Episode</button>
                    <p class="tv_show_name"><!-- {{tv_show_season.name}} : --> {{tv_shw.name}}</p>
                  </a>


# the urls 
path('Tv_watch/<str:reference_name>', views.display_tv_show, name="play_tv_show"),
    path('Watch/<str:name>', views.watch_tv_show, name="watch_tv_show"),

"""