from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .models import Task
from .serializers import TodoSerializer, RegisterSerializer, UserSerializer

# تسجيل مستخدم جديد
class RegisterAPI(APIView):
    permission_classes = [permissions.AllowAny]


    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'user': UserSerializer(user).data, 'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = response.data.get('token') if response.data else None
        if not token:
            return Response({'error': 'Invalid credentials or token not found.'}, status=status.HTTP_400_BAD_REQUEST)
        user = Token.objects.get(key=token).user
        return Response({'token': token, 'user': UserSerializer(user).data})

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['post'])
    def toggle_complete(self, request, pk=None):
        task = self.get_object()
        task.complete = not task.complete
        task.save()
        return Response(self.get_serializer(task).data)
