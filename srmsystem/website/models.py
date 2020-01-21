from django.db import models
from django.utils import timezone
from website.lib import helpers
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Simulator(models.Model):
    name = models.TextField(verbose_name="Simulator Name")
    logo = models.ImageField(verbose_name="Logo")

    def __str__(self):
        return self.name

class Server(models.Model):
    number = models.IntegerField(verbose_name="Server Number")
    address = models.TextField(verbose_name="Server Address")

    def __str__(self):
        return "Server #" + str(self.number)

    def get_url(self):
        return "steam://run/365960//+connect " + self.address

class Mod(models.Model):
    mod_types=(("Track", "Track"), ("Car", "Car"), ("Plugin", "Plugin"), ("Other", "Other"))
    name = models.TextField(verbose_name="Mod Name")
    mod_url = models.URLField(verbose_name="Download link")
    type = models.TextField(verbose_name="Mod Type", choices=mod_types)
    picture = models.ImageField(verbose_name="Picture", null=True, blank=True)
    
    def __str__(self):
        return self.name

class Track(models.Model):
    track_types=(("Road", "Road"), ("Oval", "Oval"), ("Dirt", "Dirt"), ("Snow", "Snow"))
    name = models.TextField(verbose_name="Track Name")
    type = models.TextField(verbose_name="Track Type", choices=track_types)
    length = models.FloatField(verbose_name="Track Length")
    track_map = models.ImageField(verbose_name="Track Map", null=True, blank=True)
    track_picture = models.ImageField(verbose_name="Track Picture", null=True, blank=True)
    mod = models.ForeignKey(Mod, on_delete=models.CASCADE, null=True, blank=True)
    

    def get_absolute_url(self):
        return reverse('track_details',
        args=[self.id,
            ])

    objects = models.Manager()

    def __str__(self):
        return self.name

class CarClass(models.Model):
    name = models.CharField(verbose_name="Class name", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Car classes'

class Car(models.Model):
    car_types=(("Road", "Road"), ("Oval", "Oval"), ("Dirt", "Dirt"))
    type = models.TextField(verbose_name="Car type", choices=car_types)
    manufacturer = models.CharField(verbose_name="Manufacturer", max_length=200)
    model_name = models.CharField(verbose_name="Model", max_length=200)
    mod = models.ForeignKey(Mod, on_delete=models.CASCADE, null=True, blank=True)
    carclass = models.ForeignKey(CarClass, on_delete=models.CASCADE, null=True, blank=True)
    picture = models.ImageField(verbose_name="Picture", null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse('car_details',
        args=[self.id,
            ])

    objects = models.Manager()

    def __str__(self):
        return self.manufacturer + " " + self.model_name
    
class PointSystem(models.Model):
    name=models.TextField(verbose_name="Point System Name")
    points_for_finish=models.IntegerField(verbose_name="Points for finish the race", null=True, blank=True)
    fastest_lap_points=models.IntegerField(verbose_name="Points for fastest lap", null=True, blank=True)
    pole_position_points=models.IntegerField(verbose_name="Points for pole position", null=True, blank=True)
    pos1=models.IntegerField(verbose_name="P1")
    pos2=models.IntegerField(verbose_name="P2")
    pos3=models.IntegerField(verbose_name="P3")
    pos4=models.IntegerField(verbose_name="P4")
    pos5=models.IntegerField(verbose_name="P5")
    pos6=models.IntegerField(verbose_name="P6")
    pos7=models.IntegerField(verbose_name="P7")
    pos8=models.IntegerField(verbose_name="P8")
    pos9=models.IntegerField(verbose_name="P9")
    pos10=models.IntegerField(verbose_name="P10")
    pos11=models.IntegerField(verbose_name="P11")
    pos12=models.IntegerField(verbose_name="P12")
    pos13=models.IntegerField(verbose_name="P13")
    pos14=models.IntegerField(verbose_name="P14")
    pos15=models.IntegerField(verbose_name="P15")
    pos16=models.IntegerField(verbose_name="P16")
    pos17=models.IntegerField(verbose_name="P17")
    pos18=models.IntegerField(verbose_name="P18")
    pos19=models.IntegerField(verbose_name="P19")
    pos20=models.IntegerField(verbose_name="P20")
    pos21=models.IntegerField(verbose_name="P21")
    pos22=models.IntegerField(verbose_name="P22")
    pos23=models.IntegerField(verbose_name="P23")
    pos24=models.IntegerField(verbose_name="P24")
    pos25=models.IntegerField(verbose_name="P25")
    pos26=models.IntegerField(verbose_name="P26")
    pos27=models.IntegerField(verbose_name="P27")
    pos28=models.IntegerField(verbose_name="P28")
    pos29=models.IntegerField(verbose_name="P29")
    pos30=models.IntegerField(verbose_name="P30")
    pos31=models.IntegerField(verbose_name="P31")
    pos32=models.IntegerField(verbose_name="P32")
    pos33=models.IntegerField(verbose_name="P33")
    pos34=models.IntegerField(verbose_name="P34")
    pos35=models.IntegerField(verbose_name="P35")
    pos36=models.IntegerField(verbose_name="P36")
    pos37=models.IntegerField(verbose_name="P37")
    pos38=models.IntegerField(verbose_name="P38")
    pos39=models.IntegerField(verbose_name="P39")
    pos40=models.IntegerField(verbose_name="P40")

    def __str__(self):
        return self.name
    
class Series(models.Model):
    name = models.TextField(verbose_name="Series Name")
    description = models.TextField(verbose_name="Series Description", max_length="250")
    server_password = models.CharField(verbose_name="Server Password", max_length=10, null=True, blank=True)
    isSpecialEvent=models.BooleanField(verbose_name="Series is special event", default=False)
    useSuccessBallast=models.BooleanField(verbose_name="Use Custom Success Ballast", default=False)
    simulator = models.ForeignKey(Simulator, on_delete=models.CASCADE)
    date_start=models.DateField(verbose_name="Series Starts at", null=True, blank=True)
    date_end=models.DateField(verbose_name="Series Ends at", null=True, blank=True)
    series_picture = models.ImageField(verbose_name="Series Picture", null=True, blank=True)
    series_logo = models.ImageField(verbose_name="Series Logo", null=True, blank=True)
    dnf_get_points = models.BooleanField(verbose_name="DNF Get Points", default=False)
    minimum_race_distance_for_points = models.IntegerField(verbose_name="Minimum race distance to get points")
    results_to_ignore = models.IntegerField(verbose_name="Number of driver worst results to ignore")
    team_car_results = models.IntegerField(verbose_name="Number of team cars that are awarded points for team championship")
    point_system=models.ForeignKey(PointSystem, on_delete=models.SET_NULL, null=True)
    tire_acceleration=models.IntegerField(verbose_name="Tire Degradation")
    fuel_acceleration=models.IntegerField(verbose_name="Fuel Consumption")
    abs_allowed=models.BooleanField(verbose_name="ABS")
    tc_allowed=models.BooleanField(verbose_name="TC")
    shift_allowed=models.BooleanField(verbose_name="Shift")
    clutch_allowed=models.BooleanField(verbose_name="Clutch")
    damages=models.IntegerField(verbose_name="Damage")
    cars=models.ManyToManyField(Car)

    def get_absolute_url(self):
        return reverse('series_details',
        args=[self.id,
            ])

    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'Series'

    def __str__(self):
        return self.name
    
class Challenge(models.Model):
    name=models.TextField(verbose_name="Challenge Name")
    description = models.TextField(verbose_name="Series Description", max_length="250")
    track=models.ForeignKey(Track, on_delete=models.CASCADE)
    date_start=models.DateField(verbose_name="Challenge Starts at")
    date_end=models.DateField(verbose_name="Challenge Ends at")
    picture = models.ImageField(verbose_name="Challenge Picture", null=True, blank=True)
    cars=models.ManyToManyField(Car)
    server=models.ForeignKey(Server, on_delete=models.CASCADE, null=True, blank=True)

    objects = models.Manager()
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('challenge_details',
        args=[self.id,
            ])

class Race(models.Model):
    race_length_type=(("Time", "Time"), ("Laps", "Laps"))
    start_types=(("Single File + Rolling", "Single File + Rolling"), ("Standing", "Standing"))
    weather_type=(("Scripted", "Scripted"), ("Real Weather", "Real Weather"))
    race_name=models.TextField(verbose_name="Race Name")
    description = models.TextField(verbose_name="Race Description", max_length="250", null=True, blank=True)
    race_picture = models.ImageField(verbose_name="Race Picture", null=True, blank=True)
    track=models.ForeignKey(Track, on_delete=models.CASCADE)
    race_date=models.DateTimeField(verbose_name="Race date")
    series=models.ForeignKey(Series, on_delete=models.CASCADE, null=True, blank=True, related_name="races")
    length=models.IntegerField(verbose_name="Race Length")
    length_type=models.TextField(verbose_name="Race Lenght Type", choices=race_length_type)
    series_race=models.BooleanField(verbose_name="Official Series Race")
    time_acceleration=models.IntegerField(verbose_name="Time Acceleration", default=1)
    country=models.TextField(verbose_name="Race Country", choices=helpers.GetCountiesDoubleTuple())
    real_road_coef=models.IntegerField(verbose_name="Real Road Coef.")
    start_type=models.TextField(verbose_name="Start Type", choices=start_types)
    in_sim_time=models.TimeField(verbose_name="In Sim Time")
    weather=models.TextField(verbose_name="Weather Type", choices=weather_type)
    weather_scripted_description=models.TextField(verbose_name="Scripted Weather: ", null=True, blank=True)

    def get_absolute_url(self):
        return reverse('race_details',
        args=[self.id,
            ])

    objects = models.Manager()

    def __str__(self):
        if (self.series):
            return self.series.name + " - " + self.race_name
        else:
            return self.race_name

class Qualifications(models.Model):
    qualifications_length_type=["TIME", "LAPS"]
    race=models.ForeignKey(Race, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Qualifications'

class Directories(models.Model):
    file_type=models.TextField(verbose_name="File Type")
    directory=models.FilePathField(verbose_name="Directory URL", allow_files=False, allow_folders=True)
    
    class Meta:
        verbose_name_plural = 'Directories'

class RaceResults(models.Model):
    file=models.FileField(upload_to='./results/race')
    race=models.ForeignKey(Race, on_delete=models.CASCADE)

    def __str__(self):
        return self.race.series.name + " - " + self.race.race_name

    class Meta:
        verbose_name_plural = 'Race results'
    
class QualificationsResults(models.Model):
    file=models.FileField(upload_to='./results/qual')
    race=models.ForeignKey(Race, on_delete=models.CASCADE)

    def __str__(self):
        return self.race.series.name + " - " + self.race.race_name

    class Meta:
        verbose_name_plural = 'Qualifications results'

class SeriesStandings(models.Model):
    file_name=models.TextField(verbose_name="File Name")
    class Meta:
        verbose_name_plural = 'Series Standings'

class PostCategory(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Post Categories'

    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
        unique_for_date='publish')
    author = models.ForeignKey(User,
        on_delete=models.CASCADE,
        related_name='blog_posts')
    body = models.TextField()
    picture = models.ImageField(verbose_name="Post picture", null=True, blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
        choices=STATUS_CHOICES,
        default='draft')
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE, null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse('rules_details',
        args=[self.id,
            ])

    objects = models.Manager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

class Message(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    reciepents = models.ManyToManyField(User, related_name="reciepents")
    readed_by = models.ManyToManyField(User, related_name="readed_by")

class Rules(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    series = models.ForeignKey(Series, null=True, blank=True, on_delete=models.CASCADE, related_name="rules")
    isRulesDescription = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('rules_details',
        args=[self.id,
            ])

    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'Rules'

    def __str__(self):
        return self.title