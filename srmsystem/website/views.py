from django.shortcuts import render, get_object_or_404
from .models import Race, Challenge, Post, Series, Car, Track, Rules, QualificationsResults, RaceResults
from datetime import datetime
from django.db.models import Count
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from website.lib import xmlparser, helpers
from django.utils import timezone

# Create your views here.
def homepage(request):
    today = timezone.now()
    next_races = Race.objects.order_by('race_date').filter(race_date__gte=today)[:3]
    latest_races = Race.objects.order_by('-race_date').filter(race_date__lt=today)[:3]
    challenges = Challenge.objects.all().filter(date_start__lte=today).filter(date_end__gte=today)
    posts = Post.objects.order_by('-publish')[:8]
    
    #user_data
    user_race_count = 0

    if request.user.is_authenticated:
        user_race_count = request.user.profile.races.filter(race_date__lt=today).count()

    return render(request,
                  'website/homepage.html',
                  {'next_races':next_races,
                   'latest_races':latest_races,
                   'challenges': challenges,
                   'user_race_count':user_race_count,
                   'posts':posts})

def series_list(request):
    today = datetime.today()
    current_series = Series.objects.all().order_by('-date_start').filter(date_end__gte=today).filter(isSpecialEvent=False)
    past_series=Series.objects.all().order_by('-date_start').filter(date_end__lt=today).filter(isSpecialEvent=False)


    return render(request,
                  'website/series_list.html',
                  {'current_series':current_series,
                  'past_series': past_series})

def races_list(request):
    today = timezone.now()
    next_races = Race.objects.all().order_by('race_date').filter(race_date__gte=today)
    latest_races = Race.objects.all().order_by('-race_date').filter(race_date__lt=today)

    return render(request,
                'website/races_list.html',
                {
                    'next_races':next_races,
                    'latest_races':latest_races
                })

def drivers_list(request):
    drivers_all = User.objects.all().order_by('date_joined')
    paginator = Paginator(drivers_all, 40)
    page = request.GET.get('page', 1)
    


    try:
        drivers = paginator.page(page)
    except PageNotAnInteger:
        drivers = paginator.page(1)
    except EmptyPage:
        drivers = paginator.page(paginator.num_pages)

    return render(request,'website/drivers_list.html',{
            'drivers':drivers
        })

def cars_list(request):
    cars_all = Car.objects.all()

    paginator = Paginator(cars_all, 30)
    page = request.GET.get('page', 1)
    


    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        cars = paginator.page(1)
    except EmptyPage:
        cars = paginator.page(paginator.num_pages)

    return render(request,'website/cars_list.html',{
            'cars':cars
        })

def tracks_list(request):
    tracks_all = Track.objects.all()

    paginator = Paginator(tracks_all, 30)
    page = request.GET.get('page', 1)
    


    try:
        tracks = paginator.page(page)
    except PageNotAnInteger:
        tracks = paginator.page(1)
    except EmptyPage:
        tracks = paginator.page(paginator.num_pages)

    return render(request,'website/tracks_list.html',{
            'tracks':tracks
        })

def rules_list(request):
    rules_all = Rules.objects.all().order_by('id').filter(isRulesDescription=False)
    rules_description = Rules.objects.all().order_by('id').filter(isRulesDescription=True)

    for rules in rules_all:
        print(rules.title)

    return render(request,'website/rules_list.html',{
            'rules_all':rules_all,
            'rules_description':rules_description
        })

def rules_details(request, id):
    rules = get_object_or_404(Rules, id=id)
    return render(request,
        'website/rules_details.html',
        {'rules': rules})

def car_details(request, id):
    car = get_object_or_404(Car, id=id)
    return render(request,
        'website/car_details.html',
        {'car': car})

def track_details(request, id):
    track = get_object_or_404(Track, id=id)
    return render(request,
        'website/track_details.html',
        {'track': track})

def series_details(request, id):
    series = get_object_or_404(Series, id=id)
    cars = series.cars.all()
    races = series.races.all()
    rules = series.rules.all()
    entries = series.drivers.all()
    standings = get_standings(series)
    ballast = get_ballast(series, standings)

    if request.POST:
        if series.drivers.filter(user=request.user).exists():
            series.drivers.remove(request.user.profile)
            series.save()
        else:
            series.drivers.add(request.user.profile)
            series.save()

    return render(request,
        'website/series_overview.html',
        {'series': series,
         'cars': cars,
         'races': races,
         'rules': rules,
         'entries': entries,
         'standings': standings,
         'ballast': ballast
        })

def get_standings(series):
    races = Race.objects.all().filter(series=series).filter(series_race=True).order_by('race_date')
    drivers = []

    for race in races:
        try:
            xmlfile = RaceResults.objects.get(race=race).file
        except:
            continue
        race_result = xmlparser.parse_race_results(xmlfile)
        for driver in race_result.driversRaceResults:
            if (len(drivers) == 0):
                y = DriverStandings()
                y.name = driver.name
                y.points = helpers.get_race_points(driver, race, race_result)
                drivers.append(y)
                continue
            
            if (next((x for x in drivers if x.name == driver.name), None)):
                for x in drivers:
                    if x.name == driver.name:
                        race_points = helpers.get_race_points(driver, race, race_result)
                        x.points += race_points
            else:
                y = DriverStandings()
                y.name = driver.name
                y.points = helpers.get_race_points(driver, race, race_result)
                drivers.append(y)

    return drivers

def get_ballast(series, standings):
    races = Race.objects.all().filter(series=series).filter(series_race=True).order_by('race_date')
    races_with_results = []
    for race in races:
        try:
            xmlfile = RaceResults.objects.get(race=race).file
            races_with_results.append(race)
        except:
            continue
    last_races = races_with_results[:2]
    drivers = []
    for race in races:
        try:
            xmlfile = RaceResults.objects.get(race=race).file
        except:
            continue
        race_result = xmlparser.parse_race_results(xmlfile)
        for driver in race_result.driversRaceResults:
            if driver.position < 4:
                if (len(drivers) == 0):
                    y = DriverBallast()
                    y.name = driver.name
                    if driver.position == 1:
                        y.ballast = 15
                    elif driver.position == 2:
                        y.ballast = 10
                    elif driver.position == 3:
                        y.ballast = 5
                        drivers.append(y)
                if (next((x for x in drivers if x.name == driver.name), None)):
                    for x in drivers:
                        if x.name == driver.name:
                            if driver.position == 1:
                                x.ballast += 15
                            elif driver.position == 2:
                                x.ballast += 10
                            elif driver.position == 3:
                                x.ballast += 5
                else:
                    y = DriverBallast()
                    y.name = driver.name
                    if driver.position == 1:
                        y.ballast = 15
                    elif driver.position == 2:
                        y.ballast = 10
                    elif driver.position == 3:
                        y.ballast = 5
                    drivers.append(y)

    standings_sorted = sorted(standings, key=lambda x: x.points, reverse=True)
    i = 1
    for driver in standings_sorted:
        if i == 1:
            if (len(drivers) == 0):
                y = DriverBallast()
                y.name = driver.name
                y.ballast = 15
            for x in drivers:
                if x.name == driver.name:
                    x.ballast += 15
            else:
                y = DriverBallast()
                y.name = driver.name
                y.ballast = 15
        if i == 2:
            if (len(drivers) == 0):
                y = DriverBallast()
                y.name = driver.name
                y.ballast = 10
            for x in drivers:
                if x.name == driver.name:
                    x.ballast += 10
            else:
                y = DriverBallast()
                y.name = driver.name
                y.ballast = 10
        if i == 3: 
            if (len(drivers) == 0):
                y = DriverBallast()
                y.name = driver.name
                y.ballast = 5
            for x in drivers:
                if x.name == driver.name:
                    x.ballast += 5
            else:
                y = DriverBallast()
                y.name = driver.name
                y.ballast = 5
            break
        i += 1

    return drivers


class DriverStandings():
   points = 0
   name = ""

class DriverBallast():
    ballast = 0
    name = ""


def race_details(request, id):
    race_object = get_object_or_404(Race, id=id)
    entries = race_object.drivers.all()
    is_future = False
    if race_object.race_date > timezone.now():
        is_future = True


    try:
        race_results_file = RaceResults.objects.get(race=race_object).file
        qual_results_file = QualificationsResults.objects.get(race=race_object).file
    except:
        race_results_file = None
        qual_results_file = None

    if race_results_file:
        race_results = xmlparser.parse_race_results(race_results_file)
    else:
        race_results = None

    if qual_results_file:
        qual_results = xmlparser.parse_qual_results(qual_results_file)
    else:
        qual_results = None
        
    if request.POST:
        if race_object.drivers.filter(user=request.user).exists():
            race_object.drivers.remove(request.user.profile)
            race_object.save()
        else:
            race_object.drivers.add(request.user.profile)
            race_object.save()

    return render(request,
        'website/race_details.html',{
            'race': race_object,
            'entries': entries,
            'race_results': race_results,
            'qual_results': qual_results,
            'is_future':is_future
        })

def challenge_details(request, id):
    challenge = get_object_or_404(Challenge, id=id)

    return render(request,
        'website/challenge_details.html',{
            'challenge': challenge
        })
