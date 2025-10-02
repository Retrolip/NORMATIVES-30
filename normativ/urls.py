from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from course.views import CourseViewSet

router = routers.DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
