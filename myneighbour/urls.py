from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name='welcome'),
    url('profile/', views.profile, name='profile'), 
    url(r'^profile/edit$',views.update_profile,name='edit'),   
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
