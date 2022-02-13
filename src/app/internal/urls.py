from django.urls import path
from app.internal.services.user_service import RetriveUserView, CreateUserView, UpdateUserView, ListUserView

urlpatterns = [
    path('users/', ListUserView.as_view()),
    path('users/<int:pk>/', RetriveUserView.as_view()),
    path('users/me/', RetriveUserView.as_view(), kwargs={'pk': 'me'}),
    path('users/create/', CreateUserView.as_view()),
    path('users/<int:pk>/update/', UpdateUserView.as_view()),
]
