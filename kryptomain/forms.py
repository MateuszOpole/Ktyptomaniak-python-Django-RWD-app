# -*- coding: utf-8 -*-
import sys

from django import forms
from django.contrib.auth.models import *
from django.contrib.auth.forms import UserCreationForm
from kryptomain.models import *
from django.core.mail import send_mail

class WalutaForm(forms.ModelForm):
		class Meta:
			model = Waluta
			fields = ('nazwa_waluty', 'kod_waluty',)

class KryptowalutaForm(forms.ModelForm):
		class Meta:
			model = Kryptowaluta
			fields = ('nazwa_kryptowaluty', 'kod_kryptowaluty','informacje_dodatkowe',)

class PrzelewForm(forms.ModelForm):
		class Meta:
			model = Przelew
			fields = ('nazwa_przelewu_text','kryptowaluta','ilosc_kryptowalut','data_tranzakcji','waluta_zakupu','kryptowaluta_zakupu','zaplacono','waluta_powiadomienia','widelki_min', 'widelki_max','nieaktywny')
			labels = {
            'nazwa_przelewu_text':'Nazwa przelewu',
			'kryptowaluta':'Zakupiona kryptowaluta',
			'zaplacono':'Koszt zakupu',
			'widelki_min':'Dolna granica wartości powiadomienia',
			'widelki_max':'Górna granica wartości powiadomienia',
			'waluta_powiadomienia':'Waluta sprzedaży'
			}
			widgets = {
            'data_tranzakcji': forms.DateInput(attrs={'id':'datepicker','readonly':'readonly', 'style': 'width: 100% ','class':'form-control'}),
			'waluta_zakupu': forms.Select(attrs={'id':'div1','style': 'width: 100% ','class':'form-control','style':'display:none',}),
			'kryptowaluta_zakupu':forms.Select(attrs={'id':'div2','style':'display:none','style': 'width: 100% ','class':'form-control' , 'style':'display:none'}),
			'nazwa_przelewu_text':forms.TextInput(attrs={'placeholder':'Nazwij swój przelew','style': 'width: 100% ', 'class':'form-control' }),
			'waluta_powiadomienia':forms.Select(attrs={'id':'div3','style': 'width: 100% ', 'class':'form-control' }),
			'kryptowaluta':forms.Select(attrs={'id':'div4','style': 'width: 100% ', 'class':'form-control'}),
			'widelki_min':forms.NumberInput(attrs={'style': 'width: 100% ', 'class':'form-control','type':'number'}),
			'widelki_max':forms.NumberInput(attrs={'style': 'width: 100% ', 'class':'form-control',}),
			'ilosc_kryptowalut':forms.NumberInput(attrs={'style': 'width: 100% ', 'class':'form-control'}),
			'zaplacono':forms.NumberInput(attrs={'style': 'width: 100% ', 'class':'form-control',}),
			}
			def __init__(self, *args, **kwargs):
				self.kryptowaluta_zakupu.label_class = ('div2',)
				super(PrzelewForm, self).__init__(*args, **kwargs)

class KategoriaForm(forms.ModelForm):
		class Meta:
			model = Kategoria
			fields = ('nazwa_kategorii',)
			widgets = {
            'nazwa_kategorii': forms.DateInput(attrs={'placeholder':'Wpisz kategorię','style': 'width: 100% ', 'class':'form-control'}),}

class TematycznyPostForm(forms.ModelForm):
		class Meta:
			model = TematycznyPost
			fields = ('idkategorii','nazwa_postu','text','tags')
			labels = {
            'nazwa_postu':'Temat postu',
			'text':'Tekst postu',
			'idkategorii':'Kategoria',
			'tags':'Tagi'
			}

			widgets = {
            'nazwa_postu': forms.TextInput(attrs={'placeholder':'Nazwij swój post','style': 'width: 100% ', 'class':'form-control' }),
			'text': forms.Textarea(attrs={'placeholder':'Wpisz treść','style': 'width: 100% ', 'class':'form-control' }),
			'idkategorii':forms.Select(attrs={'style': 'width: 100% ','class':'form-control' }),

			}

class KomentarzForm(forms.ModelForm):
		class Meta:
			model = Komentarz
			fields = ('textcom',)
			labels = {'textcom':'Tekst komentarza'}
			widgets = {'textcom': forms.Textarea(attrs={'placeholder':'Wpisz treść','style': 'width: 100% ', 'class':'form-control' }),
			}

class RejestracjaForm(UserCreationForm)	:
		email=forms.EmailField(required=True,error_messages={
            'invalid': ("Sprawdzam Email")},widget=forms.EmailInput(attrs={'placeholder':'Wpisz email','class':'form-control','width':'100%'}))
		password1=forms.CharField(label=("Hasło"),widget=forms.PasswordInput(attrs={'placeholder':'Wpisz hasło','class':'form-control','minlength':'8'}))
		password2 = forms.CharField(label=("Powtórz hasło"),widget=forms.PasswordInput(attrs={'placeholder':'Powtórz hasło','class':'form-control','minlength':'8'}),help_text=("Powtórz hasło dla weryfikacji."))
		error_messages = {
        'duplicate_username': ("Użytkownik o takim loginie już istnieje."),
        'password_mismatch': ("Hasła nie pasują do siebie."),
		}
		username = forms.RegexField(label=("Użytkownik"),max_length=30,
        regex=r'^[\w.@+-]+$',

        error_messages={
            'invalid': ("Można używać liter, cyfr oraz "
                         "@/./+/-/_ c.")},widget=forms.TextInput(attrs={'placeholder':'Wpisz login','class':'form-control'}))
		first_name=forms.CharField(label=("Imię"),widget=forms.TextInput(attrs={'placeholder':'Wpisz imię','class':'form-control'}))
		last_name=forms.CharField(label=("Nazwisko"),widget=forms.TextInput(attrs={'placeholder':'Wpisz nazwisko','class':'form-control'}))
		class Meta:
			model=User
			fields=(
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2')
			labels = {'password1':'Hasło',
			'username':'Nazwa użytkownika',
			'first_name':'Imię',
			'last_name':'Nazwisko',

			}
		def clean_username(self):
			username = self.cleaned_data["username"]
			try:
				User._default_manager.get(username=username)
			except User.DoesNotExist:
				return username
			raise forms.ValidationError(self.error_messages['duplicate_username'])

		def clean_password2(self):
			password1 = self.cleaned_data.get("password1")
			password2 = self.cleaned_data.get("password2")
			if password1 and password2 and password1 != password2:
				raise forms.ValidationError(
					self.error_messages['password_mismatch'])
			return password2

		def save(self, commit=True):
			user = super(RejestracjaForm, self).save(commit=False)
			user.first_name=self.cleaned_data['first_name']
			user.last_name=self.cleaned_data['last_name']
			user.email=self.cleaned_data['email']
			user.is_active = False
			if commit:
				username = self.cleaned_data["username"]
				mail_from = getattr(settings, 'DEFAULT_EMAIL', "")
				send_mail('Potwierdzenie rejestracji Kryptomaniak', 'Potwierdz rejestrację. Wejdź na stronę: https://kryptoapp2.herokuapp.com/username/'+username+'/', mail_from, [user.email, ])
				user.save()
				
				
			return user








