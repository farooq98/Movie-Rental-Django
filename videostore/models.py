from django.db import models
from datetime import datetime

class Members(models.Model):
    member_name = models.CharField(max_length=100, verbose_name="Name")
    email_address = models.CharField(max_length=100, verbose_name="Email Address", null=True, unique=True)
    age = models.PositiveIntegerField(verbose_name="Age", null=True)
    birthday = models.DateTimeField(null=True)
    gender = models.CharField(max_length=100, null=True)
    member_join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.member_name


class Movies(models.Model):
    movie_name = models.CharField(max_length=100)
    movie_year = models.IntegerField()
    movie_genere = models.CharField(max_length=100)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.movie_name


class Movie_Rental(models.Model):
    member_id = models.ForeignKey(Members, on_delete=models.CASCADE, verbose_name="Member Name")
    movie_id = models.ForeignKey(Movies, on_delete=models.CASCADE, verbose_name="Movie Name")
    rent_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField()