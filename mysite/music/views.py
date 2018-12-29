# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Album, Song
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render,get_object_or_404

class IndexView(generic.ListView):
	
	template_name = "music/index.html"
	context_object_name = 'all_albums'
	def get_queryset(self):
		return Album.objects.all()

class DetailView(generic.DetailView):
	
	model = Album
	template_name= 'music/detail.html'

class AlbumCreate(CreateView):
	model = Album
	fields = ['artist', 'album_title', 'genre', 'album_logo']
	
class AlbumUpdate(UpdateView):
	model = Album
	fields = ['artist', 'album_title', 'genre', 'album_logo']

	def get_initial(self):

		initial = super(AlbumUpdate, self).get_initial()
		print('initial data', initial)
		# retrieve current object
		album_object = self.get_object()
		initial['artist'] = album_object.artist
		initial['album_title'] = album_object.album_title
		initial['genre'] = album_object.genre
		initial['album_logo'] = album_object.album_logo
		return initial

	def get_object(self, *args, **kwargs):
		album = get_object_or_404(Album, pk=self.kwargs['pk'])
		return album

class AlbumDelete(DeleteView):
	model = Album
	success_url = reverse_lazy('music:index')


#def delete_album(request, album_id):
#    album = Album.objects.get(pk=album_id)
#    album.delete()
#    albums = Album.objects.all()
#    return render(request, 'music/index.html', {'all_albums': albums})

