from rest_framework import serializers
from .models import *
from djstripe.models import *


class StripeSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StripeSubscription
        fields = '__all__'


class MyStripeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyStripeModel
        fields = '__all__'


class MemberShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


class RefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refund
        fields = '__all__'
