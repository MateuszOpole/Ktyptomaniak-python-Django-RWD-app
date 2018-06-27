# -*- coding: utf-8 -*-
import sys
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from kryptomain.forms import *
from django.shortcuts import get_object_or_404
from kryptomain.models import *
from django.http import Http404
from django.shortcuts import redirect
from django.conf import settings
from . import models
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import *
from django.contrib.auth.models import *
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest
import json
from taggit.models import Tag
from datetime import datetime
from django.contrib.auth.models import Group
import requests
from django.core.mail import send_mail
from reportlab.pdfgen import canvas
class TagMixin(object):
    def get_context_data(self, kwargs):
        context = super(TagMixin, self).get_context_data(kwargs)
        context['tags'] = Tag.objects.all()
        return context

def home(request):
  # Return HttpRespone
  datetimenow = timezone.now()
  html = "<html><head><title>Hello workd page</title></bead><body><b>Hello</b> <i>world</i></br>It is: %s</body></html>" % datetimenow
  return HttpResponse(html)

def index(request):
	data = Kryptowaluta.objects.filter(id__gte = 1)
	postCount=TematycznyPost.objects.all().count()
	userCount=User.objects.all().count()
	przelewCount=Przelew.objects.all().count()
	datetimenow = timezone.now()
	ver=sys.version

	context={'walutaZm':data,
	'ver':ver,
	'datetimenow':datetimenow,
	'postCount':postCount,
	'userCount':userCount,
	'przelewCount':przelewCount,
	}
	return render(request, "kryptomain/index.html",context)

def info(request):
    return render(request, "kryptomain/info.html")

def Kontakt(request):
    return render(request, "kryptomain/contact.html")



# waluty

def waluty (request):
	data = Waluta.objects.all()
	context={
		'walutaZm':data
	}
	return render(request, "kryptomain/curr.html", context)

def walutaNowa (request):
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

def walutaUsun(request,cid):
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



# kryptowaluty
def Kryptowaluty (request):
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

def deleteKryptowaluta(request,cid):
	Kryptowaluta.objects.get(pk=cid).delete()
	return redirect('cryptocurrens')


#przelew
def przelewy(request):
	data = Przelew.objects.filter(ID_USER=request.user.id).order_by('data_tranzakcji').reverse()
	data2 = Kryptowaluta.objects.all();
	context={
		'przelewZm':data,
		'walutaZm':data2,
	}
	return render(request, "kryptomain/Przelewy.html", context)


def nowyPrzelew (request):
	if request.method == "POST":
		form=PrzelewForm(request.POST)
		if form.is_valid():

				c=form.save(commit=False)
				c.ID_USER=request.user.id
				c.save()
				return redirect('Przelewy')
		else:
			form=PrzelewForm()
			return render(request,"kryptomain/przelewNowy.html",{'form': form})
	else:
		form=PrzelewForm()
		return render(request,"kryptomain/przelewNowy.html",{'form': form})

def deletePrzelew(request,cid):
	Przelew.objects.get(pk=cid).delete()
	return redirect('Przelewy')

def edytujPrzelew(request,cid):
	try:
		przelew = get_object_or_404(Przelew, pk=cid)
	except przelew.DoesNotExist:
		raise Http404("Błąd pobierania waluty do edycji. Przepraszamy :/")
	if request.method == "POST":
		form=PrzelewForm(request.POST, instance=przelew)
		if form.is_valid():
				c=form.save(commit=False)

				c.save()
				return redirect('Przelewy')
	else:
		form=PrzelewForm(instance=przelew)
		idt=cid
	return render(request,"kryptomain/przelewEdycja.html",{'form': form, 'idt':idt})

def kategoria(request):
	if request.method == "POST":
		form=KategoriaForm(request.POST)
		if form.is_valid():

				"""c=Waluta()
				c.nazwa_waluty = form.cleaned_data['nazwa_waluty']
				c.kod_waluty = form.cleaned_data['kod_waluty']
				c.save()"""

				c=form.save(commit=False)
				c.save()
				return redirect('kategoria')
		else:
			data = Kategoria.objects.all();
			context={
			'kategoriaZm':data

			}
			form=KategoriaForm()
			return render(request,"kryptomain/Kategoria.html",{'form': form}, context, )
	else:
		form=KategoriaForm()
		data = Kategoria.objects.all();
		context={
		'kategoriaZm':data

		}
		return render(request,"kryptomain/Kategoria.html", context, {'form': form})

def deletekategoria (request,cid):
	Kategoria.objects.get(pk=cid).delete()
	return redirect('kategoria')

def edytujkategoria(request,cid):
	try:
		kategoria = get_object_or_404(Kategoria, pk=cid)
	except Kategoria.DoesNotExist:
		raise Http404("Błąd pobierania kategorii do edycji. Przepraszamy :/")
	if request.method == "POST":
		form=KategoriaForm(request.POST, instance=kategoria)
		if form.is_valid():
				kategoria.nazwa_kategorii = form.cleaned_data['nazwa_kategorii']

				kategoria.save()
				return redirect('kategoria')
	else:
		form=KategoriaForm(instance=kategoria)
		idt=cid
	return render(request,"kryptomain/KategoriaEdytuj.html",{'form': form, 'idt':idt})

def newtemat(request):
	if request.method == "POST":
		form=TematycznyPostForm(request.POST)
		if form.is_valid():

				c=form.save(commit=False)

				c.ID_autora=request.user
				c.data_wpisu=timezone.now()
				object=c
				object.save()
				tags = form.cleaned_data['tags']
				for tag in tags:
					object.tags.add(tag)

				return redirect('index')
		else:
			form=TematycznyPostForm()
			return render(request,"kryptomain/tematNowy.html.html",{'form': form})
	else:
		form=TematycznyPostForm()
		return render(request,"kryptomain/tematNowy.html",{'form': form})

def blog(request):
	data = TematycznyPost.objects.all().order_by('data_wpisu').reverse()
	data2 = Kategoria.objects.all();

	context={
		'PostZM':data,
		'KategoriaZM':data2,


	}
	return render(request, "kryptomain/Blog.html", context)
def blogszukaj(request):
	if request.method == 'POST':
    # Add object to database
		dataPost=request.POST

		KategoriaFiltr = dataPost['kategoria']
		filterZM = dataPost['szukaj']
		if KategoriaFiltr=='wszystkie':
			if filterZM=='':
				return redirect('blog')
			data = TematycznyPost.objects.filter(nazwa_postu__contains=filterZM)
		else:
			data = TematycznyPost.objects.filter(idkategorii_id=KategoriaFiltr, nazwa_postu__contains=filterZM).order_by('data_wpisu').reverse()
		data2 = Kategoria.objects.all();
		context={
		'PostZM':data,
		'KategoriaZM':data2,
		}
		return render(request, "kryptomain/Blog.html", context)
	else:
		return redirect('blog')
def rejestracja(request):
	if request.method == 'POST':
    # Add object to database
		form = RejestracjaForm(request.POST)
		dataPost=request.POST
		if form.is_valid():
			c=form.save()
			new_user_name=dataPost['username']
			tempUser = User.objects.get(username=new_user_name)
			my_group = Group.objects.get(name='użytkownik')
			my_group.user_set.add(tempUser)
			return redirect('index')
		else:
			args={'form':form}
			return render(request, "kryptomain/rejestracja.html",args)
	else:
		form=RejestracjaForm()
		args={'form':form}
		return render(request, "kryptomain/rejestracja.html",args)




def blogPost(request, cid):
	if request.method == "POST":
		form=KomentarzForm(request.POST)
		dataPost=request.POST
		if form.is_valid():
				c=form.save(commit=False)
				c.textcom=dataPost['textcom']
				tempPost = TematycznyPost.objects.get(pk=cid)
				c.autor=request.user
				c.data_wpisu=timezone.now()
				c.TematycznyPost=tempPost
				c.save()
				return redirect('blogPost',cid)
		else:
			data = TematycznyPost.objects.get(pk=cid)
			data2 = Kategoria.objects.all()
			data3 = Komentarz.objects.filter(TematycznyPost=data).order_by('data_wpisu').reverse()
			idt=cid
			context={
				'PostZM':data,
				'KategoriaZM':data2,
				'idt':idt,
				'KomentarzZm':data3
			}
			form = KomentarzForm()

			return render(request, "kryptomain/BlogPost.html", context, {'form': form})

	else:

		data = TematycznyPost.objects.get(pk=cid)
		data2 = Kategoria.objects.all()
		data3 = Komentarz.objects.filter(TematycznyPost=data).order_by('data_wpisu').reverse()
		idt=cid
		context={
			'PostZM':data,
			'KategoriaZM':data2,
			'idt':idt,
			'KomentarzZm':data3
		}
		forma = KomentarzForm()

		return render(request, "kryptomain/BlogPost.html", context, {'forms': forma})


def blogUser(request,slug):
	user = User.objects.get(username=slug)
	data = TematycznyPost.objects.filter(ID_autora=user)
	data2 = Kategoria.objects.all()

	context={
		'PostZM':data,
		'KategoriaZM':data2,

	}
	return render(request, "kryptomain/Blog.html", context)

def TagIndexView(request,slug):


	data = TematycznyPost.objects.filter(tags__slug__in=[slug])
	data2 = Kategoria.objects.all();
	context={

		'PostZM':data,
		'KategoriaZM':data2,
	}
	return render(request, "kryptomain/Blog.html", context)
def AktywacjaKonta(request,slug):
	user = User.objects.get(username=slug)
	user.is_active = True
	user.save()
	return render(request,"kryptomain/logowanie.html")

def pdfgenview(request):
		response = HttpResponse(content_type='application/pdf')
		response['Content-Deposition']='filename="report.pdf"'
  
		page = canvas.Canvas(response)
  
		page.setFont('Verdana',12)
  
		page.drawString(250,750, "Witaj w raporcie "+request.user.username)
		page.line(10,90,500,90)
  
	
		
  
  # ilość rekordów w tabeli Currency
  
		data = Przelew.objects.filter(ID_USER=request.user.id).order_by('data_tranzakcji').count()
		dataAktywne=Przelew.objects.filter(ID_USER=request.user.id,nieaktywny=False)
		page.drawString(10, 650, "W serwisie posiadasz ilość przelewów: " +  str(data))
		page.drawString(10, 620, "W serwisie posiadasz aktywnych przelewów, które są analizowane: " +  str(dataAktywne.count()))
		
		valuePrzelewow=checkValuePDF(request.user.id)
		page.drawString(10, 590, "Wartość aktywów, które są analizowane " +  str(round(valuePrzelewow,2))+' PLN')
		valuePrzelewow1=checkValuePDF2(request.user.id)	
		page.drawString(10, 560, "Wartość aktywów, które zostały obliczone w aplikacji  " +  str(round(valuePrzelewow1,2))+' PLN')
		przelewyBTC = Przelew.objects.filter(ID_USER=request.user.id,kryptowaluta__kod_kryptowaluty='BTC',nieaktywny=False,).count()
		page.drawString(10, 530, "Przelewy z zakupionymi BTC " +  str(przelewyBTC))
		przelewyXRP = Przelew.objects.filter(ID_USER=request.user.id,kryptowaluta__kod_kryptowaluty='XRP',nieaktywny=False,).count()
		page.drawString(10, 500, "Przelewy z zakupionymi XRP " +  str(przelewyXRP))
		przelewyETH = Przelew.objects.filter(ID_USER=request.user.id,kryptowaluta__kod_kryptowaluty='ETH',nieaktywny=False,).count()
		page.drawString(10, 470, "Przelewy z zakupionymi ETH " +  str(przelewyETH))
		page.showPage()
		page.save()
  
		return response
def logowanie(request):
		return render(request,"kryptomain/logowanie.html")

def api(request):
	if request.is_ajax():
		q = request.GET.get('term', '')
		items = Waluta.objects.filter(nazwa_waluty__startswith=q)
		result = []
		for curr in items:
			currs_json = {}
			currs_json['label'] = curr.nazwa_waluty
			currs_json['value'] = "http://127.0.0.1:8000/edytujwaluta/"+str(curr.pk)+"/"
			result.append(currs_json)
		data = json.dumps(result)
	else:
		data='fail'

	mimetype='application/json'
	return HttpResponse(data, mimetype)



def apikategoria(request):
	if request.is_ajax():
		q = request.GET.get('term', '')
		items = Kategoria.objects.filter(nazwa_kategorii__icontains=q)
		result = []
		for curr in items:
			currs_json = {}
			currs_json['label'] = curr.nazwa_kategorii
			currs_json['value'] = curr.nazwa_kategorii
			result.append(currs_json)
		data = json.dumps(result)
	else:
		data='fail'

	mimetype='application/json'
	return HttpResponse(data, mimetype)
def apiPrzelew(test):
	#Bitcoin PL
	przelewyBTCPLN = Przelew.objects.filter(kryptowaluta__kod_kryptowaluty='BTC', waluta_powiadomienia__kod_waluty='PLN',nieaktywny=False)
	apiBTCPLN = requests.get('https://api.coinmarketcap.com/v2/ticker/1/?convert=PLN')
	valueApiBTCPLN=(apiBTCPLN.json()['data']['quotes']['PLN']['price'])
	if isinstance(valueApiBTCPLN, float):
		checkValue(przelewyBTCPLN,valueApiBTCPLN,'BTC','PLN')
	#Bitcoin USD	
	przelewyBTCUSD = Przelew.objects.filter(kryptowaluta__kod_kryptowaluty='BTC', waluta_powiadomienia__kod_waluty='USD',nieaktywny=False)
	apiBTCUSD = requests.get('https://api.coinmarketcap.com/v2/ticker/1/?convert=PLN')
	valueApiBTCUSD=(apiBTCUSD.json()['data']['quotes']['USD']['price'])
	if isinstance(valueApiBTCUSD, float):
		checkValue(przelewyBTCUSD,valueApiBTCUSD,'BTC','USD')
	#Bitcoin EUR	
	przelewyBTCEUR = Przelew.objects.filter(kryptowaluta__kod_kryptowaluty='BTC', waluta_powiadomienia__kod_waluty='EUR',nieaktywny=False)
	apiBTCEUR = requests.get('https://api.coinmarketcap.com/v2/ticker/1/?convert=EUR')
	valueApiBTCEUR=(apiBTCEUR.json()['data']['quotes']['EUR']['price'])
	if isinstance(valueApiBTCEUR, float):
		checkValue(przelewyBTCEUR,valueApiBTCEUR,'BTC','EUR')
	#ETHERNEUM PLN	
	przelewyETHPLN = Przelew.objects.filter(kryptowaluta__kod_kryptowaluty='ETH', waluta_powiadomienia__kod_waluty='PLN',nieaktywny=False)
	apiETHPLN = requests.get('https://api.coinmarketcap.com/v2/ticker/1027/?convert=PLN')
	valueApiETHPLN=(apiETHPLN.json()['data']['quotes']['PLN']['price'])
	if isinstance(valueApiETHPLN, float):
		checkValue(przelewyETHPLN,valueApiETHPLN,'ETH','PLN')
	#ETHERNEUM EUR	
	przelewyETHEUR = Przelew.objects.filter(kryptowaluta__kod_kryptowaluty='ETH', waluta_powiadomienia__kod_waluty='EUR',nieaktywny=False)
	apiETHEUR = requests.get('https://api.coinmarketcap.com/v2/ticker/1027/?convert=EUR')
	valueApiETHEUR=(apiETHEUR.json()['data']['quotes']['EUR']['price'])
	if isinstance(valueApiETHEUR, float):
		checkValue(przelewyETHEUR,valueApiETHEUR,'ETH','EUR')
	#ETHERNEUM USD
	przelewyETHUSD = Przelew.objects.filter(kryptowaluta__kod_kryptowaluty='ETH', waluta_powiadomienia__kod_waluty='USD',nieaktywny=False)
	apiETHUSD = requests.get('https://api.coinmarketcap.com/v2/ticker/1027/?convert=PLN')
	valueApiETHUSD=(apiETHUSD.json()['data']['quotes']['USD']['price'])
	if isinstance(valueApiETHUSD, float):
		checkValue(przelewyETHUSD,valueApiETHUSD,'ETH','USD')
	 #Ripple PLN
	przelewyXRPPLN = Przelew.objects.filter(kryptowaluta__kod_kryptowaluty='XRP', waluta_powiadomienia__kod_waluty='PLN',nieaktywny=False)
	apiXRPPLN= requests.get('https://api.coinmarketcap.com/v2/ticker/52/?convert=PLN')
	valueApiXRPPLN=(apiETHPLN.json()['data']['quotes']['PLN']['price'])
	if isinstance(valueApiXRPPLN, float):
		checkValue(przelewyXRPPLN,valueApiXRPPLN,'XRP','PLN')
	#Ripple EUR
	przelewyXRPEUR = Przelew.objects.filter(kryptowaluta__kod_kryptowaluty='XRP', waluta_powiadomienia__kod_waluty='EUR',nieaktywny=False)
	apiXRPEUR= requests.get('https://api.coinmarketcap.com/v2/ticker/52/?convert=EUR')
	valueApiXRPEUR=(apiXRPEUR.json()['data']['quotes']['EUR']['price'])
	if isinstance(valueApiXRPEUR, float):
		checkValue(przelewyXRPEUR,valueApiXRPEUR,'XRP','EUR')
	#Ripple USD
	przelewyXRPUSD = Przelew.objects.filter(kryptowaluta__kod_kryptowaluty='XRP', waluta_powiadomienia__kod_waluty='USD',nieaktywny=False)
	apiXRPUSD= requests.get('https://api.coinmarketcap.com/v2/ticker/52/?convert=PLN')
	valueApiXRPUSD=(apiXRPUSD.json()['data']['quotes']['USD']['price'])
	if isinstance(valueApiXRPUSD, float):
		checkValue(przelewyXRPUSD,valueApiXRPUSD,'XRP','USD')
	
	return HttpResponse()
#	
	 #Ethereum Pl
	# apiETH = requests.get('https://api.coinmarketcap.com/v2/ticker/1027/?convert=PLN')
	 #ripple
	# apiXRP= requests.get('https://api.coinmarketcap.com/v2/ticker/52/?convert=PLN')
def checkValue(przelewy, valueApi, Kryptowaluta,Waluta ):
	for przelew in przelewy:
			value= float ( przelew.ilosc_kryptowalut)*valueApi
			tempEmail = User.objects.values_list('email', flat=True).get(id=przelew.ID_USER)
			if float(przelew.widelki_max)<value:
				mail_from = getattr(settings, 'DEFAULT_EMAIL', "")
				send_mail('uwaga powiadomienie kryptomaniak', 'Granica górna przekroczona: '+ str(przelew.ilosc_kryptowalut)+' '+Kryptowaluta +' warte: '+str(round(value,3))+Waluta, mail_from, [tempEmail, ])
			if float(przelew.widelki_min)>value:
				mail_from = getattr(settings, 'DEFAULT_EMAIL', "")
				send_mail('uwaga powiadomienie kryptomaniak', 'Granica dolna:przekroczona:'+ str(przelew.ilosc_kryptowalut)+' '+Kryptowaluta +' warte: '+str(round(value,3))+Waluta, mail_from, [tempEmail, ])
	return 
def checkValuePDF(user_id):

	value=float(0)
	przelewyBTCPLN = Przelew.objects.filter(ID_USER=user_id,kryptowaluta__kod_kryptowaluty='BTC',nieaktywny=False,)
	apiBTCPLN = requests.get('https://api.coinmarketcap.com/v2/ticker/1/?convert=PLN')
	valueApiBTCPLN=(apiBTCPLN.json()['data']['quotes']['PLN']['price'])
	
	przelewyETHPLN = Przelew.objects.filter(ID_USER=user_id,kryptowaluta__kod_kryptowaluty='ETH',nieaktywny=False)
	apiETHPLN = requests.get('https://api.coinmarketcap.com/v2/ticker/1027/?convert=PLN')
	valueApiETHPLN=(apiETHPLN.json()['data']['quotes']['PLN']['price'])
	
	przelewyXRPPLN = Przelew.objects.filter(ID_USER=user_id,kryptowaluta__kod_kryptowaluty='XRP',nieaktywny=False)
	apiXRPPLN= requests.get('https://api.coinmarketcap.com/v2/ticker/52/?convert=PLN')
	valueApiXRPPLN=(apiETHPLN.json()['data']['quotes']['PLN']['price'])
	if isinstance(valueApiXRPPLN, float):
		checkValue(przelewyXRPPLN,valueApiXRPPLN,'XRP','PLN')
	
	for przelew in przelewyBTCPLN:
		if isinstance(valueApiBTCPLN, float):
			value=value+(valueApiBTCPLN*float(przelew.ilosc_kryptowalut))
	for przelew in przelewyETHPLN :
		if isinstance(valueApiETHPLN, float):
			value=value+(valueApiETHPLN*float(przelew.ilosc_kryptowalut))			
	for przelew in przelewyXRPPLN:
		if isinstance(valueApiXRPPLN, float):
			value=value+(valueApiXRPPLN*float(przelew.ilosc_kryptowalut))	
	return value
				
def checkValuePDF2(user_id):

	value=float(0)
	przelewyBTCPLN = Przelew.objects.filter(ID_USER=user_id,kryptowaluta__kod_kryptowaluty='BTC',nieaktywny=True)
	apiBTCPLN = requests.get('https://api.coinmarketcap.com/v2/ticker/1/?convert=PLN')
	valueApiBTCPLN=(apiBTCPLN.json()['data']['quotes']['PLN']['price'])
	
	przelewyETHPLN = Przelew.objects.filter(ID_USER=user_id,kryptowaluta__kod_kryptowaluty='ETH',nieaktywny=True)
	apiETHPLN = requests.get('https://api.coinmarketcap.com/v2/ticker/1027/?convert=PLN')
	valueApiETHPLN=(apiETHPLN.json()['data']['quotes']['PLN']['price'])
	
	przelewyXRPPLN = Przelew.objects.filter(ID_USER=user_id,kryptowaluta__kod_kryptowaluty='XRP',nieaktywny=True)
	apiXRPPLN= requests.get('https://api.coinmarketcap.com/v2/ticker/52/?convert=PLN')
	valueApiXRPPLN=(apiETHPLN.json()['data']['quotes']['PLN']['price'])
	if isinstance(valueApiXRPPLN, float):
		checkValue(przelewyXRPPLN,valueApiXRPPLN,'XRP','PLN')
	
	for przelew in przelewyBTCPLN:
		if isinstance(valueApiBTCPLN, float):
			value=value+(valueApiBTCPLN*float(przelew.ilosc_kryptowalut))
	for przelew in przelewyETHPLN :
		if isinstance(valueApiETHPLN, float):
			value=value+(valueApiETHPLN*float(przelew.ilosc_kryptowalut))			
	for przelew in przelewyXRPPLN:
		if isinstance(valueApiXRPPLN, float):
			value=value+(valueApiXRPPLN*float(przelew.ilosc_kryptowalut))	
	return value
					
def apiPost(request):
	if request.is_ajax():
		q = request.GET.get('term', '')
		items = TematycznyPost.objects.filter(nazwa_postu__startswith=q)
		result = []
		for postZm in items:
			post_json = {}
			post_json['label'] = postZm.nazwa_postu
			post_json['value'] = postZm.nazwa_postu
			result.append(post_json)
		data = json.dumps(result)
	else:
		data='fail'

	mimetype='application/json'
	return HttpResponse(data, mimetype)