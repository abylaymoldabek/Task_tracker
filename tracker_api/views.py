from django.http import HttpResponse
from .serializers import TaskSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .tasks import send_mail
from rest_framework.response import Response


class TaskViewSet(ModelViewSet):
    # permission_classes = [GuestPermission | AdminPermission | EmployeePermission]
    permission_classes = IsAuthenticated,
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # def list(self, request, *args, **kwargs):
    #     send_mail.delay()
    #     return HttpResponse()

    def partial_update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        serializer.complete(self.get_object(), serializer.data.get('status'))
        super(TaskViewSet, self).partial_update(request, *args, **kwargs)
        send_mail(pk=self.get_object().id).delay()
        return Response(TaskSerializer(self.get_object()).data)
