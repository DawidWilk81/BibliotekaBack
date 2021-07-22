
from django.urls import path, include
from rest_framework import routers
from .views import KsiazkaViewSet, UserViewSet, UserRegister, CustomAuthToken
from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()
router.register('users', UserViewSet),
router.register('Ksiazki', KsiazkaViewSet),
router.register('register', UserRegister),


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', ObtainAuthToken.as_view()),
    path('api-token-auth/', CustomAuthToken.as_view()),

]
