# -*- coding: utf-8 -*-
import sys



from django.shortcuts import render, redirect
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

import sys
import json
from taggit.models import Tag
from datetime import datetime
from django.contrib.auth.models import Group

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


def pdfgenview(request):
		return render(request,"kryptomain/logowanie.html")
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
		items = Kategoria.objects.filter(nazwa_kategorii__startswith=q)
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