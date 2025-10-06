from rest_framework.routers import DefaultRouter
from .views import CovidRecordViewSet
from django.contrib import admin
from django.urls import path, include

router = DefaultRouter()
router.register(r'data', CovidRecordViewSet, basename='covid')

urlpatterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('covid.urls')),
]
