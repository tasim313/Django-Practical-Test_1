from django.shortcuts import render
from djstripe.models import *
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


class Product(viewsets.ModelViewSet):

    """Product means Data Plan"""
    """Product Get, Post, Update and Delete. Here Admin can add product, user can see products and product details.Admin add new product and Delete product and update product"""

    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class Price(viewsets.ModelViewSet):

    """Price Get, Post, Update and Delete. Here Admin can add product price, user can see products price and product price details.Admin add new product price and Delete product price and update product price"""

    permission_classes = [IsAuthenticated]
    serializer_class = PriceSerializer
    queryset = Price.objects.all()


class Plan(viewsets.ModelViewSet):

    """Data Plan Get, Post, Update and Delete. Here Admin can add product plan, user can see products plan and product plan details.Admin add new product plan and Delete product plan and update product plan"""

    permission_classes = [IsAuthenticated]
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()


class Refund(viewsets.ModelViewSet):

    """Money Refund Get, Post, Update and Delete. Here  user can see refund details. Admin add new refund and Delete refund and update refund"""

    permission_classes = [IsAuthenticated]
    serializer_class = RefundSerializer
    queryset = Refund.objects.all()


class StripeSubscription(APIView):

    """Here user can create new subscription.If any user create a subscription and subscription can not cancel or Delete User can not create new subscription"""
    """User can input start date and insert subscription status"""

    permission_classes = [IsAuthenticated]
    serializer_class = StripeSubscriptionSerializer

    def post(self, request):
        start_date = request.data.get('start_date')
        status = request.data.get('status')
        already_register = StripeSubscription.objects.filter(status=status)
        if already_register.exists():
            return Response("Already Save in DataBase", status=status.HTTP_200_OK)
        else:
            data = {'start_date': start_date, 'status': status}

            serializer = StripeSubscriptionSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyStripe(APIView):

    """Here user can create new subscription.If any user create a subscription and subscription can not cancel or Delete User can not create new subscription"""
    """User can insert his/her name, phone number. Phone number is unique"""

    permission_classes = [IsAuthenticated]
    serializer_class = MyStripeModelSerializer

    def post(self, request):
        name = request.data.get('name')
        phone_number = request.data.get('phone_number')
        stripe_subscription = request.data.get('stripe_subscription')
        already_register = MyStripeModel.objects.filter(phone_number=phone_number)
        if already_register.exists():
            return Response("Already Save in DataBase", status=status.HTTP_200_OK)
        else:
            data = {'name': name, 'phone_number': phone_number, 'stripe_subscription': stripe_subscription}

            serializer = MyStripeModelSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Membership(APIView):

    """Here user can create a membership. If any user create a new membership and membership can not cancel or Delete User can not create new membership"""

    permission_classes = [IsAuthenticated]
    serializer_class = MemberShipSerializer

    def post(self, request):
        user = request.data.get('user')
        customer = request.data.get('customer')
        already_register = MyStripeModel.objects.filter(user=user)
        if already_register.exists():
            return Response("Already Save in DataBase", status=status.HTTP_200_OK)
        else:
            data = {'user': user, 'customer': customer}

            serializer = MemberShipSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)