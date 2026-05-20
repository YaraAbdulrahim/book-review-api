from django.urls import path
from .views import (
    RegisterView,
    BookListCreateView,
    BookDetailView,
    ReviewListCreateView,
    ReviewDetailView,
    ChangePasswordView,
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    # Authentication
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Books
    path('books/', BookListCreateView.as_view(), name='books'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Reviews
    path('books/<int:book_id>/reviews/', ReviewListCreateView.as_view(), name='book-reviews'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),

    # Change Password
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]