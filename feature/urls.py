from rest_framework import routers
from rest_framework import urlpatterns
from .api import FeatureViewSet

router = routers.DefaultRouter()
router.register('api/features', FeatureViewSet, 'features')

urlpatterns = router.urls