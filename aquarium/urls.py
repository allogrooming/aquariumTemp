from django.contrib import admin
from django.urls import path, include
import mainApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test', mainApp.views.test),
    path('', include('mainApp.urls')),
]
