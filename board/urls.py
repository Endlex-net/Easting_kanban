from rest_framework import routers
from board import views

router = routers.DefaultRouter()
router.register('task', views.TaskViewSet)
router.register('project', views.ProjectViewSet)

urlpatterns = router.urls
