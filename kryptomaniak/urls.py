"""kryptomaniak URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from kryptomain import views
from django.contrib.auth import views as auth_views

from django.conf.urls import include, url

urlpatterns = [
	url(r'^newprzelew/', views.nowyPrzelew, name='nowyPrzelew'),
	url(r'^rejestracja/',views.rejestracja, name="rejestracja"),
	url(r'^blogUser/(?P<slug>[-\w]+)/$', views.blogUser, name='blogUser'),
	url(r'^blogPost/(?P<cid>\d+)/$', views.blogPost, name='blogPost'),
	url(r'^api/', views.api, name='api'),
	url(r'^apiPost/', views.apiPost, name='apiPost'),
	url(r'^blogszukaj', views.blogszukaj, name='blogszukaj'),
	url(r'^blog/', views.blog, name='blog'),
	url(r'^taggit/', include('taggit_selectize.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^apikategoria/', views.apikategoria, name='apikategoria'),
	url(r'^newtemat/', views.newtemat, name='newtemat'),
	url(r'^tag/(?P<slug>[-\w]+)/$', views.TagIndexView, name='tagged'),
	url(r'^logowanie/',views.logowanie, name="logowanie"),
	url(r'^login/$', auth_views.login, {'template_name' : 'kryptomain/index.html'}, name='login'),
	url(r'^logout/$', auth_views.logout, {'next_page' : 'index'}, name='logout'),
	url(r'^pdfgenview/',views.pdfgenview, name="pdfgenview"),
	url(r'^edytujPrzelew/(?P<cid>\d+)/$', views.edytujPrzelew, name='edytujPrzelew'),
	url(r'^deletePrzlew/(?P<cid>\d+)/$', views.deletePrzelew, name='usunPrzelew'),
	url(r'^deletekryptowaluta/(?P<cid>\d+)/$', views.deleteKryptowaluta, name='usunKryptowaluta'),
	url(r'^deletewaluta/(?P<cid>\d+)/$', views.walutaUsun, name='usunwaluta'),
	url(r'^deletekategoria/(?P<cid>\d+)/$', views.deletekategoria, name='deletekategoria'),
	url(r'^edytujkryptowaluta/(?P<cid>\d+)/$', views.edytujKryptowaluta, name='edytujKryptowaluta'),
	url(r'^edytujwaluta/(?P<cid>\d+)/$', views.edytujwaluta, name='edytujwaluta'),
	url(r'^edytujkategoria/(?P<cid>\d+)/$', views.edytujkategoria, name='edytujkategoria'),
	url(r'^newcryptocurr/', views.nowaKryptoWaluta, name='nowaKryptoWaluta'),
	
	url(r'^newcurr/', views.walutaNowa, name='nowawal'),	
	url(r'^kategoria/', views.kategoria, name='kategoria'),
	url(r'^curr/', views.waluty, name='currens'),	
	url(r'^przelewy/', views.przelewy, name='Przelewy'),	
	url(r'^cryptocurr/', views.Kryptowaluty, name='cryptocurrens'),
	url(r'^home/', views.home),	
    url(r'^info/', views.info, name='informacja'),
	url(r'^kontakt/', views.Kontakt,  name='kontakt'),
    url(r'^admin/', admin.site.urls),
	url(r'', views.index, name='index' ),
	
	
	
]
