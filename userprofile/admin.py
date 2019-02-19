from django.contrib import admin
from .models import UserProfile, UserGame
# from .forms import StatusForm

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'birth_date', 'gender', 'phone_no', 'show_games']

    # def show_games(self, obj):
    #     return "\n".join([a.name for a in obj.games.all()])

    def show_games(self, obj):
        return ", ".join([
            game.name for game in obj.player_games.all()
        ])

    show_games.short_description = "games"

class UserGameAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'player', 'game']

# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserGame, UserGameAdmin)

