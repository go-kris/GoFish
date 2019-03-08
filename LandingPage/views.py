from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from .forms import EmailForm
# Create your views here.


def guides(request):
    if request.method == 'POST':
        return send_mail("Test Subject", "Test Subjet", "blake@go-fish.io", ['blake@go-fish.io'],
		 html_message="<html>Test of html message</html>")

    else:
        form = EmailForm()
    return render(request, 'guides.html', {'form': form})


def fisherman(request):
    return render(request, 'fisherman.html')


def choose(request):
    return render(request, 'choose.html')
