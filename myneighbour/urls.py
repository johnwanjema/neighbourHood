from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name='welcome'),
    url(r'^profile/edit$',views.update_profile,name='edit'),
    url('profile/', views.profile, name='profile'),
    url('^newhood',views.addneighbourhood,name="hood"),
    url(r'^new_business/(?P<pk>\d+)$',views.new_business,name='new_business'),
    url(r'^hood_details/(?P<neighbourhood_id>\d+)/$' , views.hood_details, name='detail' ),
    url(r'^new_post/(?P<pk>\d+)$',views.new_post,name='new_post'),
    url(r'^search/', views.search,name='search'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
