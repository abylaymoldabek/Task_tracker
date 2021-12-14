# from .permissions import GuestPermission, AdminPermission, EmployeePermission
from .serializers import TaskSerializer
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny


from .models import Task


class TaskViewSet(ModelViewSet):
    # permission_classes = [GuestPermission | AdminPermission | EmployeePermission]
    permission_classes = IsAuthenticated,
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
