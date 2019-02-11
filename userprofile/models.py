from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from game.models import Game




class UserProfileQuerySet(models.QuerySet):
    pass

class UserProfileManager(models.Manager):
    def get_queryset(self):
        return UserProfileQuerySet(self.model, using=self._db)

class UserProfile(models.Model):


    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # user = models.One(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    birth_date = models.DateField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    phone_no = PhoneNumberField(blank=True)
    objects = UserProfileManager()
    player_games = models.ManyToManyField(Game, blank=True, related_name='games')


    def __str__(self):
        return str(self.user.username)[:50]


# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)
#
# post_save.connect(create_user_profile, sender=User)