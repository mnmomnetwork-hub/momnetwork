from rest_framework.routers import DefaultRouter
from .views import WinnerViewSet

router = DefaultRouter()
router.register(r"winners", WinnerViewSet, basename="winners")

urlpatterns = router.urls
