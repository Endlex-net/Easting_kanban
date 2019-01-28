from rest_framework import routers
from account import views

router = routers.DefaultRouter()
router.register('auth', views.AuthViewSet)
router.register('member', views.MemberViewSet)
router.register('department', views.DepartmentViewSet)

urlpatterns = router.urls
