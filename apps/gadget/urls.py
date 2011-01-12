from django.conf.urls.defaults import *


urlpatterns = patterns('gadget',
  (r'^$', 'views.getCountyTopArtists'),
  #(r'^gcta/$', 'views.get_country_top_artist'),
  #(r'^lastfm/$', 'views.lastfm_data'),
  (r'^user_list/$','views.get_user_list'),
  (r'^plist/$','views.get_plist'),
  (r'^tracks/(?P<name>.*)','views.getTopTracks'),
  (r'^save/','views.save_to_playlist'),
  (r'^delete/','views.delete'),
  #(r'^save/(?P<mbid>[A-Za-z0-9-_]*)/(?P<itemid>\d+)/','views.save_to_playlist'),
  #(r'^save/test/99/','views.save_to_playlist'),
   
  #(r'^lastfm/', 'lastfm.views.lastfm_data'),
  #
  #(r'^gadget/', 'views.playlist'),
)
