from django.contrib.auth.models import User
from django.shortcuts import render

from rest_framework.permissions import AllowAny
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book, Review

from .serializers import (
    RegisterSerializer,
    BookSerializer,
    ReviewSerializer
)


# HOME PAGE
def home(request):

    return render(
        request,
        'home.html'
    )


# REGISTER
class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()

    serializer_class = RegisterSerializer


# BOOKS
class BookListCreateView(generics.ListCreateAPIView):

    queryset = Book.objects.all()

    serializer_class = BookSerializer

    permission_classes = [AllowAny]


# BOOK DETAIL
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Book.objects.all()

    serializer_class = BookSerializer

    permission_classes = [AllowAny]


# REVIEWS
class ReviewListCreateView(generics.ListCreateAPIView):

    serializer_class = ReviewSerializer

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get_queryset(self):

        book_id = self.kwargs['book_id']

        return Review.objects.filter(
            book_id=book_id
        )

    def perform_create(self, serializer):

        book_id = self.kwargs['book_id']

        serializer.save(
            user=self.request.user,
            book_id=book_id
        )


# REVIEW UPDATE DELETE
class ReviewDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    queryset = Review.objects.all()

    serializer_class = ReviewSerializer

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def perform_update(self, serializer):

        serializer.save(
            user=self.request.user
        )

    def delete(self, request, *args, **kwargs):

        review = self.get_object()

        if review.user != request.user:

            return Response(
                {'error': 'Not allowed'}
            )

        return super().delete(
            request,
            *args,
            **kwargs
        )

    def put(self, request, *args, **kwargs):

        review = self.get_object()

        if review.user != request.user:

            return Response(
                {'error': 'Not allowed'}
            )

        return super().put(
            request,
            *args,
            **kwargs
        )


# CHANGE PASSWORD
class ChangePasswordView(APIView):

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def post(self, request):

        user = request.user

        new_password = request.data.get(
            'new_password'
        )

        user.set_password(new_password)

        user.save()

        return Response(
            {'message': 'Password changed'}
        )