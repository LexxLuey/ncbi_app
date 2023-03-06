# -*- encoding: utf-8 -*-
import datetime

from django import forms
from django.contrib.auth.models import User
from .models import Student


class StudentForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "First Name", "class": "form-control"})
    )
    middle_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Last Name", "class": "form-control"}
        ),
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Last Name", "class": "form-control"}
        ),
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Email", "class": "form-control"}),
        max_length=200,
    )
    gender = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "form-control"}),        
        choices=Student.GENDER
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "23490123456789", "class": "form-control"}),
        max_length=200,
    )
    year_of_growth_track_completion = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    contact_address = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Address", "class": "form-control"}
        ),
    )
    age_range = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "form-control"}),        
        choices=Student.AGE_RANGE
    )
    marital_status = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "form-control"}),        
        choices=Student.MARITAL_CHOICES
    )
    centre = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "form-control"}),        
        choices=Student.CENTRE_CHOICES
    )
    service_team = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Protocol", "class": "form-control"}
        ),
    )
    home_cell_group = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Dominion Cell", "class": "form-control"}
        ),
    )
    cell_church_colony = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "C3", "class": "form-control"}
        ),
    )
    passport_photo = forms.ImageField(
        widget=forms.FileInput(
            attrs={"placeholder": "Passport", "class": "form-control"}
        ),
    )