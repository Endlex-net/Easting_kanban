from rest_framework import routers
from account import views

router = routers.DefaultRouter()
router.register('member', views.MemberViewSet)

urlpatterns = router.urls
