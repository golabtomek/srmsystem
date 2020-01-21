from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('series/', views.series_list, name='series'),
    path('races/', views.races_list, name='races'),
    path('drivers/', views.drivers_list, name='drivers'),
    path('cars/', views.cars_list, name='cars'),
    path('tracks/', views.tracks_list, name='tracks'),
    path('rules/', views.rules_list, name='rules'),
    path('rules/<int:id>', views.rules_details, name='rules_details'),
    path('series/<int:id>', views.series_details, name='series_details'),
    path('race/<int:id>', views.race_details, name='race_details'),
    path('challenge/<int:id>', views.challenge_details, name='challenge_details'),
    path('cars/<int:id>', views.car_details, name='car_details'),
    path('track/<int:id>', views.track_details, name='track_details')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)