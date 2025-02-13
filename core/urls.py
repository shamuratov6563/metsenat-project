"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from app.views import index
from orm.views import orm


def home(request, a, b):
    c = a + b
    return HttpResponse(f"<h1>{a} + {b} = {c}</h1>")

def hisoblash(request, matn:str):
    digit_count = 0
    alpha_count = 0
    for i in matn:
        if i.isalpha():
            alpha_count += 1
        elif i.isdigit():
            digit_count += 1
    return HttpResponse(f"<h1> raqamlar: {digit_count}, harflar: {alpha_count}")

def search(request, matn):
    return HttpResponse(f"<a href='http://google.com/search?q={matn}'>Go to Google</a>")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:a>/<int:b>/', home),
    # path('<str:matn>/', hisoblash),
    path('qidiruv/<str:matn>/', search),
    path('index/', index),
    path('', orm)
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)