from rest_framework.response import Response
from rest_framework import generics, status
from app.internal.serializers.serializers import UserSerializer
from app.internal.models.telegram_user import TelegramUser


class ListUserView(generics.ListAPIView):
    queryset = TelegramUser.objects.all()
    serializer_class = UserSerializer


class RetriveUserView(generics.RetrieveAPIView):
    queryset = TelegramUser.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        if self.kwargs.get('pk', None) == 'me':
            self.kwargs['pk'] = self.request.user.pk
        return super(RetriveUserView, self).get_object()


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UpdateUserView(generics.UpdateAPIView):
    queryset = TelegramUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
