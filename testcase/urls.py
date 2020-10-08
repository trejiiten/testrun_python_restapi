from rest_framework import routers
from rest_framework import urlpatterns
from .api import TestcaseViewSet

router = routers.DefaultRouter()
router.register('api/testcases', TestcaseViewSet, 'testcases')

urlpatterns = router.urls