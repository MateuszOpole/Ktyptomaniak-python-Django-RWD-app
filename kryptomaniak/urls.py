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
from django.conf.urls import url
from django.contrib import admin
from kryptomain import views

urlpatterns = [
	url(r'^deletekryptowaluta/(?P<cid>\d+)/$', views.deleteKryptowaluta, name='usunKryptowaluta'),
	url(r'^deletewaluta/(?P<cid>\d+)/$', views.deletewaluta, name='usunwaluta'),
	url(r'^edytujkryptowaluta/(?P<cid>\d+)/$', views.edytujKryptowaluta, name='edytujKryptowaluta'),
	url(r'^edytujwaluta/(?P<cid>\d+)/$', views.edytujwaluta, name='edytujwaluta'),
	url(r'^newcryptocurr/', views.nowaKryptoWaluta, name='nowaKryptoWaluta'),
	url(r'^newprzelew/', views.nowyPrzelew, name='nowyPrzelew'),
	url(r'^newcurr/', views.newcurr, name='nowawal'),	
	url(r'^curr/', views.curr, name='currens'),	
	url(r'^cryptocurr/', views.cryptocurr, name='cryptocurrens'),
	url(r'^home/', views.home),	
    url(r'^info/', views.info, name='informacja'),
	url(r'^kontakt/', views.contact,  name='kontakt'),
    url(r'^admin/', admin.site.urls),
	url(r'', views.index, name='index' )
	
	
]
