from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import UserProfileViewSet, ProductViewSet, OrderViewSet, NotificationViewSet
from book import views

router = routers.DefaultRouter()
router.register(r'user_profiles', UserProfileViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('create_user/', views.create_user, name='create_user'),
    path('', include(router.urls)),
]


