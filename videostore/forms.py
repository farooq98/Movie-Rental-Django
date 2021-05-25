from django import forms
from datetime import datetime
from django.core.exceptions import ValidationError
from . import models

class DateInput(forms.DateInput):
    input_type = 'date'

class MovieForm(forms.ModelForm):
    CHOICES = [
        ("Action", "Action"),
        ("Drama", "Drama"),
        ("Thriller", "Thriller"),
        ("Comedy", "Comedy"),
        ("Other", "Other")
    ]
    movie_year = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    movie_genere = forms.ChoiceField(choices = CHOICES, widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = models.Movies
        fields = ['movie_name', 'movie_year', 'movie_genere', 'price']
        widgets = {
            'movie_name': forms.TextInput(attrs={'class':'form-control'})
        }
    
    def clean_price(self):
        price = self.cleaned_data["price"]
        if price < 0:
            raise ValidationError("Invalid Price")
        return price

    def clean_movie_year(self):
        year = self.cleaned_data["movie_year"]
        if year > datetime.now().date().year:
            raise ValidationError("Invalid year")
        return year
    

class MemberForm(forms.ModelForm):
    CHOICES = [
        (1, "Male"),
        (2, "Female"),
        (3, "Other"),
        (4, "Rather Not Say")
    ]
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    birthday = forms.DateInput()
    email_address = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    gender = forms.ChoiceField(choices = CHOICES, widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = models.Members
        fields = ['member_name', 'email_address', 'age', 'birthday', 'gender']
        widgets = {
            'member_name': forms.TextInput(attrs={'class':'form-control'}),
            'email_address': forms.TextInput(attrs={'class':'form-control'}),
            'birthday': DateInput(attrs={'class':'form-control'}),
        }

    def clean_birthday(self):
        birthday = self.cleaned_data["birthday"]
        if birthday.date() > datetime.now().date():
            raise ValidationError("Invalid Birthday")
        return birthday

    def clean_age(self):
        age = self.cleaned_data["age"]
        if age < 0:
            raise ValidationError("Invalid Age")
        return age

class MovieRentalForm(forms.ModelForm):

    return_date = forms.DateInput()
    
    class Meta:
        model = models.Movie_Rental
        fields = ['member_id', 'movie_id', 'return_date']
        widgets = {
            'member_id': forms.Select(attrs={'class':'form-control', 'readonly':'readonly'}),
            'movie_id': forms.Select(attrs={'class':'form-control', 'readonly':'readonly'}),
            'return_date': DateInput(attrs={'class':'form-control'}),
        }
    
    def clean_return_date(self):
        return_date = self.cleaned_data['return_date']
        if return_date.date() < datetime.now().date():
            raise ValidationError("Invalid return date")
        return return_date

class MemberNameForm(forms.Form):

    Choices = [(data['id'], data['member_name']) for data in models.Members.objects.all().values('member_name', 'id')]
    member_name = forms.ChoiceField(choices = Choices, widget=forms.Select(attrs={'class':'form-control'}))


