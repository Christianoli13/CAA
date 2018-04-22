from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('caa/', include('caa.urls')),
    path('admin/', admin.site.urls),
]

