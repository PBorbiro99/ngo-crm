from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from . import views
from users.views import UserViewSet
from donors.views import DonorViewSet, DonationViewSet
from projects.views import ProjectViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'donors', DonorViewSet)
router.register(r'donations', DonationViewSet)
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('donors/', views.donor_list, name='donor_list'),
    path('projects/', views.project_list, name='project_list'),
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)