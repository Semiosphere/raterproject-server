from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from raterprojectapi.views import register_user, login_user
from rest_framework import routers
from raterprojectapi.views import GameView
from raterprojectapi.views import RatingView
from raterprojectapi.views import ReviewView
from raterprojectapi.views import CategoryView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'games', GameView, 'game')
router.register(r'ratings', RatingView, 'rating')
router.register(r'reviews', ReviewView, 'review')
router.register(r'categories', CategoryView, 'category')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]