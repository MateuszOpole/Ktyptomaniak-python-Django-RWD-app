from django.db import models

# Create your models here.

class Waluta(models.Model):
	nazwa_waluty = models.CharField(max_length=50)
	kod_waluty = models.CharField(max_length=10)
	def __str__(self):
			return self.nazwa_waluty
	
	
	
class Kryptowaluta(models.Model):
	nazwa_kryptowaluty = models.CharField(max_length=50)
	kod_kryptowaluty = models.CharField(max_length=10)
	def __str__(self):
			return self.nazwa_kryptowaluty
	
	
class Przelew(models.Model):
	ID_USER = models.IntegerField(default=0)
	nazwa_przelewu_text = models.CharField(max_length=70)
	kryptowaluta = models.ForeignKey(Kryptowaluta)
	ilość_kryptowalut = models.DecimalField(max_digits=10, decimal_places=4)
	waluta = models.ForeignKey(Waluta)
	zaplacono=models.DecimalField(max_digits=10, decimal_places=4)
	data_tranzakcji = models.DateTimeField('Data zakupu waluty')
	def __str__(self):
			return self.nazwa_przelewu_text