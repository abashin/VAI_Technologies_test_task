from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="VAI_Technologies_test_task API",
        default_version='v1',
        description="VAI_Technologies_test_task",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="VAI_Technologies_test_task@VAI_Technologies_test_task.com"),
        license=openapi.License(name="VAI_Technologies_test_task License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include(router.urls)),
]
