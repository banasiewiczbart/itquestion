from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .forms import RequestForm
from .models import RequestModel
from django.urls import reverse_lazy
from django.views.generic import CreateView
from itquestion_app.forms import SignUpForm


def show_request(request):
    return render(request, "request.html")

def done_request_view(request):
    return render(request, "done_request.html")

def no_login_request_view(request):
    return render(request, "no-login_request.html")

# Sign Up View
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy ('login')
    template_name = 'registration/signup.html'



def calendar_view(request):
    return render  (request, "calendar.html")

@login_required #widok się nie wykona, ale ustaw stronę z poleceniem i schowaj przyciski
def make_request_view(request):
    # if request.method == 'GET':
    #
    #     return render(request, '/request.html')
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/done_request_screen") #stwórz Gratulacje dodaj elsa





    # else:
    #     form = RequestForm()
    # return render(request, "request.html")
