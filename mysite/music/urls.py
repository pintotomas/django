from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
	# /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    #/music/71/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /music/album/album/add
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
 
     # /music/album/album/2/
    url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/album/2/delete
    url(r'^(?P<pk>[0-9]+)/delete_album/$', views.AlbumDelete.as_view(), name='delete_album'),
    #url(r'^(?P<album_id>[0-9]+)/delete_album/$', views.delete_album, name='delete_album'),
]