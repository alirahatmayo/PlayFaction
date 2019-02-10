from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# from userprofile.models import UserProfile


class GameQuerySet(models.QuerySet):
    pass

class GameManager(models.Manager):
    def get_queryset(self):
        return GameQuerySet(self.model, using=self._db)

class Game(models.Model):

    GENRE_CHOICES = (
        ('ac', 'Action'),
        ('sh', 'Shooter'),
        ('st', 'Strategy'),
        ('rc', 'Race'),
        ('o', 'Other'),
        ('sp', 'Sports'),
    )


    # user = models.ForeignKey(settings.AUTH_USER_MODEL, unique=True, on_delete=models.CASCADE)
    # player = models.ManyToManyField(UserProfile, null=True)
    # Release  = models.DateField(null=True)
    name = models.CharField(null=True, max_length=240)
    genre = models.CharField(max_length=10, choices=GENRE_CHOICES, null=True)
    description = models.TextField(null=True, max_length=100)

    objects = GameManager()

    def __str__(self):
        return self.name
