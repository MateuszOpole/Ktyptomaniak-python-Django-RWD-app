from django import forms

from kryptomain.models import *

class WalutaForm(forms.ModelForm):
		class Meta:
			model = Waluta
			fields = ('nazwa_waluty', 'kod_waluty',)

class KryptowalutaForm(forms.ModelForm):
		class Meta:
			model = Kryptowaluta
			fields = ('nazwa_kryptowaluty', 'kod_kryptowaluty',)
			
class PrzelewForm(forms.ModelForm):
		class Meta:
			model = Przelew
			fields = ('kryptowaluta',)
			
			
		