from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import CustomUser
from .forms import SighUpForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.db.models.signals import post_save

def home(request):
    return render(request, 'home.html')


class SighUp(CreateView):
    model = User
    form_class = SighUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        birthday = form.cleaned_data['birthday']
        picture = form.files[0]
        address = form.cleaned_data['address']
        post_save.send(sender=User, instance = self.get_object(), created=True,
        profile_data={
            'birthday':birthday,
            'picture': picture,
            'address':address
        })
        return response