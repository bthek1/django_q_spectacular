from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import ToDo
from .serializers import ToDoSerializer
from .tasks import complete_todo_later
import os
from django.shortcuts import render
from django.http import Http404

class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all().order_by('-created_at')
    serializer_class = ToDoSerializer

    # Add custom action to mark ToDo as completed asynchronously
    @action(detail=True, methods=['get','post', 'put'])
    def mark_completed(self, request, pk=None):
        todo = self.get_object()  # Retrieve the specific ToDo item
        if todo.is_completed:
            return Response({"detail": "This ToDo is already completed."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Trigger the asynchronous task to mark it as completed
        complete_todo_later(todo.id)
        
        return Response({"detail": "The task to complete the ToDo is running in the background."}, status=status.HTTP_202_ACCEPTED)



def documentation_view(request, path='index.html'):
    return render(request, 'docs/index.html')
    # # Ensure the path is safe
    # if '..' in path or path.startswith('/'):
    #     raise Http404("Invalid path")

    # # Build the full path to the documentation file
    # template_path = os.path.join('docs', path)

    # # Check if the template exists
    # if not os.path.isfile(os.path.join('django_q_spectacular/templates', template_path)):
    #     raise Http404("Page not found")

    # return render(request, template_path)