from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from kryptomain.forms import *
from django.shortcuts import get_object_or_404
from kryptomain.models import *
from django.http import Http404
from django.shortcuts import redirect
from . import models
from . import forms

import sys
def home(request):
  # Return HttpRespone
  datetimenow = timezone.now()
  html = "<html><head><title>Hello workd page</title></bead><body><b>Hello</b> <i>world</i></br>It is: %s</body></html>" % datetimenow
  return HttpResponse(html)

def index(request):
  datetimenow = timezone.now()
  ver=sys.version
  return render(request, "kryptomain/index.html",{'datetime':datetimenow,'ver':ver})

def info(request):
    return render(request, "kryptomain/info.html")

def contact(request):
    return render(request, "kryptomain/contact.html")


def curr (request):
	data = Waluta.objects.all()
	context={
		'walutaZm':data
	}
	return render(request, "kryptomain/curr.html", context)

def cryptocurr (request):
	data = Kryptowaluta.objects.all()
	context={
		'walutaZm':data
	}
	return render(request, "kryptomain/listaKryptowalut.html", context)

def nowaKryptoWaluta (request):
	if request.method == "POST":
		form=KryptowalutaForm(request.POST)
		if form.is_valid():
				
				"""c=Waluta()
				c.nazwa_waluty = form.cleaned_data['nazwa_waluty']
				c.kod_waluty = form.cleaned_data['kod_waluty']
				c.save()"""
				
				c=form.save(commit=False)
				c.save()
				return redirect('cryptocurrens')
		else:
			form=KryptowalutaForm()
			return render(request,"kryptomain/kryptowalutaNowa.html",{'form': form})
	else:
		form=KryptowalutaForm()
		return render(request,"kryptomain/kryptowalutaNowa.html",{'form': form})
		
def nowyPrzelew (request):
	if request.method == "POST":
		form=PrzelewForm(request.POST)
		if form.is_valid():
				
				"""c=Waluta()
				c.nazwa_waluty = form.cleaned_data['nazwa_waluty']
				c.kod_waluty = form.cleaned_data['kod_waluty']
				c.save()"""
				
				c=form.save(commit=False)
				c.save()
				return redirect('cryptocurrens')
		else:
			form=PrzelewForm()
			return render(request,"kryptomain/przelewNowy.html",{'form': form})
	else:
		form=PrzelewForm()
		return render(request,"kryptomain/przelewNowy.html",{'form': form})

def deleteKryptowaluta(request,cid):
	Kryptowaluta.objects.get(pk=cid).delete()
	return redirect('cryptocurrens')
	
def edytujKryptowaluta(request,cid):
	try:
		waluta = get_object_or_404(Kryptowaluta, pk=cid)
	except Waluta.DoesNotExist:
		raise Http404("Błąd pobierania waluty do edycji. Przepraszamy :/")
	if request.method == "POST":
		form=KryptowalutaForm(request.POST, instance=waluta)
		if form.is_valid():
				waluta.nazwa_kryptowaluty = form.cleaned_data['nazwa_kryptowaluty']
				waluta.kod_kryptowaluty = form.cleaned_data['kod_kryptowaluty']
				waluta.save()
				return redirect('cryptocurrens')
	else:
		form=KryptowalutaForm(instance=waluta)
		idt=cid
	return render(request,"kryptomain/kryptowalutaEdycja.html",{'form': form, 'idt':idt})


def newcurr (request):
	if request.method == "POST":
		form=WalutaForm(request.POST)
		if form.is_valid():
				
				"""c=Waluta()
				c.nazwa_waluty = form.cleaned_data['nazwa_waluty']
				c.kod_waluty = form.cleaned_data['kod_waluty']
				c.save()"""
				
				c=form.save(commit=False)
				c.save()
				return redirect('currens')
		else:
			form=WalutaForm()
			return render(request,"kryptomain/walutaNowa.html",{'form': form})
	else:
		form=WalutaForm()
		return render(request,"kryptomain/walutaNowa.html",{'form': form})

def deletewaluta(request,cid):
	Waluta.objects.get(pk=cid).delete()
	return redirect('currens')
	
def edytujwaluta(request,cid):
	try:
		waluta = get_object_or_404(Waluta, pk=cid)
	except Waluta.DoesNotExist:
		raise Http404("Błąd pobierania waluty do edycji. Przepraszamy :/")
	if request.method == "POST":
		form=WalutaForm(request.POST, instance=waluta)
		if form.is_valid():
				waluta.nazwa_waluty = form.cleaned_data['nazwa_waluty']
				waluta.kod_waluty = form.cleaned_data['kod_waluty']
				waluta.save()
				return redirect('currens')
	else:
		form=WalutaForm(instance=waluta)
		idt=cid
	return render(request,"kryptomain/walutaEdycja.html",{'form': form, 'idt':idt})
