from django.shortcuts import render, redirect
from django.views.generic import (
    View,
)
from .forms import StudentForm
from .models import Student
from pprint import pprint

class HomeView(View):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        context = dict()

        # messages.success(request, "Matters Loaded Successfully.")
        return render(request, self.template_name, context)


class RegisterView(View):
    template_name = "registration/signup.html"

    def get(self, request, *args, **kwargs):
        form = StudentForm()

        return render(request, self.template_name, {"form": form})
    
    def post(self, request, *args, **kwargs):
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            # p = Student.objects.create(**form.cleaned_data)
            return redirect("/")
        # messages.success(request, "Matters Loaded Successfully.")
        return render(request, self.template_name, {"form": form})