from rest_framework import routers
from rest_framework import urlpatterns
from .api import EnvironmentViewSet

router = routers.DefaultRouter()
router.register('api/environment', EnvironmentViewSet, 'environment')

urlpatterns = router.urls