from django.urls import path, include
from .views import home
from rest_framework.routers import DefaultRouter
from .views import IPOViewSet

router = DefaultRouter()
router.register(r'ipo', IPOViewSet)  # Creates /api/ipo/ endpoint

urlpatterns = [
    path('', home, name='home'),            # Homepage route
    path('api/', include(router.urls)),     # API route
]
