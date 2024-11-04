from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
urlpatterns = [
    path('login',login),
    path('', user_list, name='telegram_users'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)