from .models import Game
from django.contrib import admin

# from .forms import StatusForm
#
class GameAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'genre', 'description']

    # def show_players(self, obj):
    #     return "\n".join([a.user_name for a in obj.user.all()])

# Register your models here.
admin.site.register(Game, GameAdmin)
