from django.conf.urls import url


from SoundCloudApp.Views import api_views, albums_views, songs_views, general_views


urlpatterns = [
    #Django Views
    url(r'^albums/$', albums_views.AlbumIndex.as_view(), name="index"),
    url(r'^albums/(?P<pk>[0-9]+)/$', albums_views.AlbumDetail.as_view(), name="detail"),
    url(r'^album/add/$', albums_views.AlbumCreate.as_view(), name="album-add"),
    url(r'^album/(?P<pk>[0-9]+)/update/$', albums_views.AlbumUpdate.as_view(), name="album-update"),
    url(r'^album/(?P<pk>[0-9]+)/delete/$', albums_views.AlbumDelete.as_view(), name="album-delete"),
    url(r'^album/(?P<pk>[0-9]+)/fav/$', albums_views.AlbumFavourite.as_view(), name="album-fav"),


    url(r'^songs/$', songs_views.SongView.as_view(), name="songs"),
    url(r'^album/(?P<pk>[0-9]+)/song/add/$', songs_views.SongCreate.as_view(), name="song-add"),
    url(r'^song/(?P<pk>[0-9]+)/delete/$', songs_views.SongDelete.as_view(), name="song-delete"),
    url(r'^song/(?P<pk>[0-9]+)/fav/$', songs_views.SongFavourite.as_view() , name="song-fav"),

    url(r'^search/$', general_views.Search.as_view(), name="search"),
    url(r'^fav_albums/$', general_views.FavouritesView.as_view(), name="fav_albums"),

    #######################################################
    #Rest framework API views
    url(r'^api/users/$', api_views.UserList.as_view()),
    url(r'^api/create_user/$', api_views.UserCreate.as_view()),
    url(r'^api/users/(?P<pk>[0-9]+)/$', api_views.UserDetail.as_view()),
    url(r'^api/users/(?P<pk>[0-9]+)/delete/$', api_views.UserDelete.as_view()),

    url(r'^api/albums/$', api_views.AlbumList.as_view()),
    url(r'^api/create_album/$', api_views.AlbumCreate.as_view()),
    url(r'^api/albums/(?P<pk>[0-9]+)/$', api_views.AlbumDetail.as_view()),
    url(r'^api/albums/(?P<pk>[0-9]+)/update/$', api_views.AlbumUpdate.as_view()),
    url(r'^api/albums/(?P<pk>[0-9]+)/delete/$', api_views.AlbumDelete.as_view()),

    url(r'^api/songs/$', api_views.SongList.as_view()),
    url(r'^api/create_song/$', api_views.SongCreate.as_view()),
    url(r'^api/song/(?P<pk>[0-9]+)/delete/$', api_views.SongDelete.as_view()),
]
