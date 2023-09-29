from django.contrib import admin
from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from items import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cakes/', views.CakesApi.as_view(), name='cakes'),
    path('cakes/<int:pk>/', views.CakesDeleteApi.as_view(), name='del-cake'),
]


urlpatterns += [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/schema/swagger-ui/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/schema/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
]
