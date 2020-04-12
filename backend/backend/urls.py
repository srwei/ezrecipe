from django.contrib import admin
from django.urls import path, include                 # add this
from rest_framework import routers                    # add this

router = routers.DefaultRouter()                      # add this

urlpatterns = [
    path('', include('ezrecipe.urls')),
    path('admin/', admin.site.urls),        
    path('api/', include(router.urls))                # add this
]