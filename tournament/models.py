from django.db import models
from django.contrib.auth.models import User
# from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from game.models import Game



class TournamentQuerySet(models.QuerySet):
    pass

class TournamentManager(models.Manager):
    def get_queryset(self):
        return TournamentQuerySet(self.model, using=self._db)

class Tournament(models.Model):

    #
    # GENDER_CHOICES = (
    #     ('m', 'Male'),
    #     ('f', 'Female'),
    #     ('o', 'Other'),
    # )


    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    # birth_date = models.DateField(null=True)
    # gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    # phone_no = PhoneNumberField(blank=True)
    # objects = UserProfileManager()
    # player_games = models.ManyToManyField(Game, null=True, related_name='games')

    name = models.CharField(null=True, max_length=240)
    description = models.TextField(null=True, max_length=1000)
    reg_before = models.DateTimeField(null=True)
    date = models.DateTimeField(null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    participants = models.ManyToManyField(User, related_name='participants', blank= True)
    # player_games = models.ManyToManyField(Game, blank=True, related_name='games')

    def __str__(self):
        return str(self.name)[:50]


# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)
#
# post_save.connect(create_user_profile, sender=User)