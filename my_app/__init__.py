# python manage.py shell
# from my_app.models.task import Task, SubTask
# from datetime import datetime, timedelta
# from django.utils import timezone
# >>> task = Task.objects.create(
# ...     title="Prepare presentation",
# ...     description="Prepare materials and slides for the presentation",
# ...     status="New",
# ...     deadline=today + timedelta(days=3)
# ... )

# SubTask.objects.create(
#     title="Gather information",
#     description="Find necessary information for the presentation",
#     task=task,
#     status="New",
#     deadline=timezone.now() + timedelta(days=2)
# )

# SubTask.objects.create(
#     title="Create slides",
#     description="Create presentation slides",
#     task=task,
#     status="New",
#     deadline=timezone.now() + timedelta(days=1)
# )

# new_tasks = Task.objects.filter(status="New")
# for task in new_tasks:
#     print(task)

# expired_done_subtasks = SubTask.objects.filter(status="Done", deadline__lt=timezone.now())
# for subtask in expired_done_subtasks:
#   print(subtask)

# task.status = "In Progress"
# task.save()

# gather_info_subtask = task.subtasks.get(title="Gather information")
# gather_info_subtask.deadline = timezone.now() - timedelta(days=2)
# gather_info_subtask.save()

# create_slides_subtask = task.subtasks.get(title="Create slides")
# create_slides_subtask.description = "Create and format presentation slides"
# create_slides_subtask.save()

#task.delete()
