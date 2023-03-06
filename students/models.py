# from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.urls import reverse

# CFC Abuja, CFC Gboko, CFC Makurdi, CFC Kaduna, CFC Sagamu, CFC Lagos, CFC Otukpo, CFC Benin
# Single, Marrried, Divorced, Widowed
# <Month> | <Female> (Growth Track Started in 2020, so we need to customize the years from then)
# 18-25, 26-30, 31-35, 36-40, 41-45, 46-50, Above 50


class Mixin(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class Centre(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("Centre")
        verbose_name_plural = _("Centres")

    def __str__(self):
        return f"CFC {self.name}"

    def get_absolute_url(self):
        return reverse("centre_detail", kwargs={"pk": self.pk})


class ServiceTeam(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("service team")
        verbose_name_plural = _("service teams")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("service_team_detail", kwargs={"pk": self.pk})


class HomeCellGroup(models.Model):
    name = models.CharField(max_length=100)
    centre = models.ForeignKey(Centre, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home_cell_group_detail", kwargs={"pk": self.pk})


class Student(Mixin):
    GENDER = (
        ("Male", "Male"),
        ("Female", "Female")
    )

    AGE_RANGE =(
        (
            "18-25",
            "18-25",
        ),
        (
            "26-30",
            "26-30",
        ),
        (
            "31-35",
            "31-35",
        ),
        (
            "36-40",
            "36-40",
        ),
        (
            "41-45",
            "41-45",
        ),
        (
            "46-50",
            "46-50",
        ),
        (
            "Above 50", 
            "Above 50"
        )

    )

    MARITAL_CHOICES = (
        ("Single", "Single"),
        ("Marrried", "Marrried"),
        ("Divorced", "Divorced"),
        ("Widowed", "Widowed")
    )

    CENTRE_CHOICES = (
        ("CFC Abuja", "CFC Abuja"),
        ("CFC Gboko", "CFC Gboko"),
        ("CFC Makurdi", "CFC Makurdi"),
        ("CFC Kaduna", "CFC Kaduna"),
        ("CFC Sagamu", "CFC Sagamu"),
        ("CFC Lagos", "CFC Lagos"),
        ("CFC Otukpo", "CFC Otukpo"),
        ("CFC Benin", "CFC Benin")
    )

    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    middle_name = models.CharField(_("middle name"), max_length=150)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), blank=True)
    gender = models.CharField(
        max_length=20,
        choices=GENDER,
        default=GENDER[0],
    )
    phone_number = models.CharField(max_length=100)
    contact_address = models.CharField(max_length=100)
    age_range = models.CharField(
        max_length=10,
        choices=AGE_RANGE,
        default=AGE_RANGE[0],
    )
    marital_status = models.CharField(
        max_length=20,
        choices=MARITAL_CHOICES,
        default=MARITAL_CHOICES[0],
    )
    centre = models.CharField(
        max_length=100,
        choices=CENTRE_CHOICES,
        default=CENTRE_CHOICES[0],
    )
    year_of_growth_track_completion = models.DateField(
        _("year of growth track completion"),
        auto_now=False,
        auto_now_add=False,
        null=True,
    )
    service_team = models.CharField(max_length=100)
    home_cell_group = models.CharField(max_length=100)
    cell_church_colony = models.CharField(max_length=100)
    passport_photo = models.ImageField(upload_to='passports/', blank=True, null=True)

    class Meta:
        verbose_name = _("student")
        verbose_name_plural = _("students")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
