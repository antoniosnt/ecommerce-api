from django.urls import path, include
from rest_framework.routers import DefaultRouter
from jestor.jst_products.views import ProductViewSet
from jestor.jst_categories.views import CategoryViewSet

router = DefaultRouter()

router.register(r"products", ProductViewSet, basename="product")
router.register(r"categories", CategoryViewSet, basename="category")

urlpatterns = [path("", include(router.urls))]
