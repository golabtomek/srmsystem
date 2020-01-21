from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Simulator)
admin.site.register(Mod)
admin.site.register(Track)
admin.site.register(CarClass)
admin.site.register(Car)
admin.site.register(PointSystem)
admin.site.register(Series)
admin.site.register(Challenge)
admin.site.register(Race)
admin.site.register(Qualifications)
admin.site.register(Directories)
admin.site.register(RaceResults)
admin.site.register(QualificationsResults)
admin.site.register(SeriesStandings)
admin.site.register(PostCategory)
admin.site.register(Message)
admin.site.register(Rules)
admin.site.register(Server)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish',
        'status', 'category')
    list_filter = ('status', 'created', 'publish', 'author', 'category')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
