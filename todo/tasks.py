from django_q.tasks import async_task
from .models import ToDo
import time

def mark_completed(todo_id):
    # Simulating a long-running task
    time.sleep(10)
    todo = ToDo.objects.get(id=todo_id)
    todo.is_completed = True
    todo.save()

def complete_todo_later(todo_id):
    async_task('todo.tasks.mark_completed', todo_id)
