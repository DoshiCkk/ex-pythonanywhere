from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.views import home, SighUp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('signup/', SighUp.as_view(), name='signup'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)