from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """Контроллер предоставляет действия CRUD для регистрации нового пользователя."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        """Обработка создания нового пользователя."""

        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
