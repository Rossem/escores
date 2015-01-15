from django.contrib import admin
from main.models import *

# Register your models here.

class PlayerInline(admin.TabularInline):
    model = Player
    extra = 5

"""
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, {'fields': ['question_text']}),
            ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ]

    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text'](admin.TabularInline):
    model = Match
    extra = 3
    pass
"""

class TeamAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, {'fields': ['team_name', 'team_name_abr', 'game', 'league'], 'classes': 'extrapretty'})
        ]
    inlines = [PlayerInline]
    model = Team
    extra = 5


admin.site.register(Team, TeamAdmin)
admin.site.register(Game)
admin.site.register(Stats)
admin.site.register(League)
admin.site.register(Match)
admin.site.register(News)
admin.site.register(Region)
