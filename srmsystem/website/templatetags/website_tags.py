from django import template
from ..models import Post, Rules, PointSystem
from django.db.models import Count
from ..lib import xmlparser, helpers
from django.utils.safestring import mark_safe
from django.utils import timezone
from account.models import Profile
from django.contrib.auth.models import User
import datetime
import markdown

register = template.Library()

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))

@register.filter(name="timedelta")
def timedelta(timedeltaobj):
    delta = datetime.timedelta(seconds=timedeltaobj)
    return str(delta)[:-3]

@register.filter(name="timedelta_without_h")
def timedelta_without_h(timedeltaobj):
    delta = datetime.timedelta(seconds=timedeltaobj)
    remove_h = str(delta)[2:]
    return remove_h[:-3]

#@register.filter(name="get_race_points")
#def get_race_points(driver, race):
#    points = helpers.get_race_points(driver, race)
#   return points

@register.simple_tag()
def get_race_points(driver, race, race_result):
    return helpers.get_race_points(driver, race, race_result)

@register.filter(name="check_if_registered_series")
def check_if_registered_series(user,series):
    registered = False
    for user_series in user.profile.series.all():
        if series == user_series:
            registered = True
            break
    return registered

@register.filter(name="check_if_registered_race")
def check_if_registered_race(user,race):
    registered = False
    for user_races in user.profile.races.all():
        if race == user_races:
            registered = True
            break
    return registered

@register.filter(name="check_if_future_race")
def check_if_future_race(race):
    today = timezone.now()
    is_future = False
    if race.race_date > today:
        is_future = True
    return is_future

@register.simple_tag()
def join_series(user, series):
    done = False
    if series.drivers.filter(user=user).exists():
        done = True
    else:
        series.drivers.add(user.profile)
        done = True
    return done
    
