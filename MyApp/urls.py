from django.urls import path, include
from .views import *
from rest_framework import routers
router = routers.SimpleRouter()
router.register(r'product', Product, basename="product")
router.register(r'price', Price, basename="price")
router.register(r'plan', Plan, basename='plan')
router.register(r'refund', Refund, basename='refund')

urlpatterns = [
    path('MyStripe/', MyStripe.as_view(), name='MyStripeModel'),
    path('membership/', Membership.as_view(), name='membership'),
    path('subscription/', StripeSubscription.as_view(), name='subscription'),
]+router.urls