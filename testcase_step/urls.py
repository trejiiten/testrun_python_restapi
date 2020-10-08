from rest_framework import routers
from rest_framework import urlpatterns
from .api import TestcaseStepViewSet

router = routers.DefaultRouter()
router.register('api/testcase_steps', TestcaseStepViewSet, 'testcase_steps')

urlpatterns = router.urls