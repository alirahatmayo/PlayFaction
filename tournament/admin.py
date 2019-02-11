from django.contrib import admin
from .models import Tournament


class TournamentAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'game',  'reg_before', 'description', 'date', 'show_participants']

    # def show_games(self, obj):
    #     return "\n".join([a.name for a in obj.games.all()])

    def show_participants(self, obj):
        return ", ".join([
            a.username for a in obj.participants.all()
        ])

    show_participants.short_description = "participants"



    # def show_games(self, obj):
    #     return ", ".join([
    #         game.name for game in obj.player_games.all()
    #     ])
    #
    # show_games.short_description = "games"

# Register your models here.


# Register your models here.
admin.site.register(Tournament, TournamentAdmin)