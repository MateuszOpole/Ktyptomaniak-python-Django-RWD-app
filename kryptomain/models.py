# -*- coding: utf-8 -*-
import sys


from django.db import models
from datetime import date
import datetime
from taggit.managers import TaggableManager
from django.conf import settings
# Create your models here.





class Waluta(models.Model):
	nazwa_waluty = models.CharField(max_length=50)
	kod_waluty = models.CharField(max_length=10)
	def __str__(self):
			return self.nazwa_waluty



class Kryptowaluta(models.Model):
	nazwa_kryptowaluty = models.CharField(max_length=50)
	kod_kryptowaluty = models.CharField(max_length=10)
	informacje_dodatkowe = models.CharField(max_length=50, default='Strona internetowa')
	def __str__(self):
			return self.nazwa_kryptowaluty


class Przelew(models.Model):
	ID_USER = models.IntegerField(default=0)
	nazwa_przelewu_text = models.CharField(max_length=70)
	kryptowaluta = models.ForeignKey(Kryptowaluta)
	ilosc_kryptowalut = models.DecimalField(max_digits=10, decimal_places=4)
	waluta_zakupu = models.ForeignKey(Waluta, default=0, related_name='%(class)s_waluta_zakupu')
	kryptowaluta_zakupu = models.ForeignKey(Kryptowaluta, default=0,  related_name='%(class)s_kryptowaluta_zakupu')
	zaplacono=models.DecimalField(max_digits=10, decimal_places=4)
	data_tranzakcji = models.DateField('Data zakupu waluty', default=date.today)
	waluta_powiadomienia = models.ForeignKey(Waluta, default=0, related_name='%(class)s_waluta_powiadomienia')
	widelki_min=models.DecimalField(max_digits=10, decimal_places=4, default=0)
	widelki_max=models.DecimalField(max_digits=10, decimal_places=4, default=0)
	def __str__(self):
			return self.nazwa_przelewu_text

class Kategoria(models.Model):
	nazwa_kategorii = models.CharField(max_length=70)
	def __str__(self):
		return self.nazwa_kategorii


class TematycznyPost(models.Model):
	ID_autora = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	data_wpisu = models.DateTimeField('data wpisu', default=datetime.datetime.now())
	nazwa_postu = models.CharField(max_length=70)
	text = models.TextField()
	tags = TaggableManager()

	idkategorii= models.ForeignKey(Kategoria, default=0)
	def __str__(self):
		return self.nazwa_postu

class Komentarz(models.Model):
	autor = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	data_wpisu = models.DateTimeField('data wpisu',default=datetime.datetime.now())
	textcom = models.TextField(max_length=300)
	TematycznyPost=models.ForeignKey(TematycznyPost,default=0)



class Like(models.Model):
	ID_USER = models.IntegerField(default=0)
	idPost = models.ForeignKey(TematycznyPost)
	values = models.IntegerField(default=0)







