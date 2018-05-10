from django.conf.urls import url, include
from rest_framework import routers
from map.views import ShopViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(r'shops', ShopViewSet)
router.register(r'products', ProductViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]