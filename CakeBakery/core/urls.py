from django.urls import path
from . import views


#    to include media file-------

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path ('',views.index,name='index'),
    path ('about/',views.about,name='about')

]

#  this is the media folder

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
